import datetime
from typing import List

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny
from restaurant.models import Restaurant, Menu
from restaurant.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    MenuListSerializer,
    RestaurantListSerializer,
    VoteSerializer,
    VoteListSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class RestaurantViewSet(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return RestaurantListSerializer
        return RestaurantSerializer

    def get_permissions(self) -> List[BasePermission]:
        if self.action in ["list","retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class MenuViewSet(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


    def get_serializer_class(self):
        if self.action == "list":
            return MenuListSerializer
        if self.action in ["choose_place", "today_results"]:
            return VoteSerializer
        return MenuSerializer

    def get_permissions(self) -> List[BasePermission]:
        if self.action in ["list","retrieve","today_results"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(
        methods=["get", "post"],
        detail=False,
        url_path="choose_place_for_today",
        serializer_class=None,
    )
    def choose_place(self, request):
        now = datetime.datetime.now()
        day_of_week = now.weekday()
        if request.method == "GET":
            queryset = Menu.objects.filter(daily_menu=day_of_week)
            serializer = VoteListSerializer(queryset, many=True)

            return Response(serializer.data)
        elif request.method == "POST":
            serializer = VoteSerializer(
                data=request.data
            )
            if serializer.is_valid():

                restaurant = Restaurant.objects.get(
                    name=serializer.validated_data.get("restaurant")
                )
                menu = Menu.objects.filter(daily_menu=day_of_week).get(
                    restaurant=restaurant
                )
                if not serializer.validated_data.get("restaurant"):
                    return Response({"message": "You should choose restaurant"})
                # Проверка на то голосовал ли юзер за ресторан уже
                if request.user in menu.users_voted.all():
                    return Response(
                        {"message": "You already voted for this restaurant"}
                    )

                restaurant.votes += serializer.validated_data.get("vote")
                menu.users_voted.add(request.user)
                restaurant.save()
                menu.save()
                return Response({"message": "Rating submitted successfully"})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        methods=[
            "get",
        ],
        detail=False,
        url_path="today_results",
        serializer_class=None,
    )
    def today_results(self, request):
        now = datetime.datetime.now()
        day_of_week = now.weekday()
        if request.method == "GET":
            queryset = (
                Menu.objects.filter(daily_menu=day_of_week)
                .order_by("-restaurant__votes")
                .first()
            )
            serializer = VoteListSerializer(queryset, many=False)

            return Response(serializer.data)
