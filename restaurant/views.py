import datetime

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.db.models import QuerySet
from restaurant.models import Restaurant, Menu
from restaurant.serializers import RestaurantSerializer, MenuSerializer, MenuListSerializer, RestaurantListSerializer, \
    VoteSerializer, VoteListSerializer
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


    # @staticmethod
    # def get_daily_menu_number(day):
    #     """
    #     Метод для получения номера дня недели по его значению (строковому представлению)
    #     """
    #     for number, display_value in Menu.DAYS_OF_WEEK_CHOICES:
    #         if display_value.lower() == day.lower():
    #             return number
class MenuViewSet(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()




    def get_serializer_class(self):
        if self.action == "list":
            return MenuListSerializer
        if self.action == "choose_place":
            return VoteSerializer
        return MenuSerializer

    @action(methods=['get', 'post'], detail=False, url_path="choose_place", serializer_class=None)
    def choose_place(self, request):
        now = datetime.datetime.now()
        day_of_week = now.weekday()
        # Логика обработки GET-запроса
        if request.method == 'GET':

            queryset = Menu.objects.filter(daily_menu=day_of_week)
            serializer = VoteListSerializer(queryset, many=True)

            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = VoteSerializer(data=request.data)  # Используем MenuListSerializer
            if serializer.is_valid():
                # Валидация данных ресторана
                print(serializer.validated_data.get('restaurant'))
                if not serializer.validated_data.get('restaurant'):
                    return Response({'message': 'You should choose restaurant'})
                print(serializer.validated_data.get('vote'))
                restaurant = Restaurant.objects.get(name=serializer.validated_data.get('restaurant'))
                restaurant.votes += serializer.validated_data.get('vote')
                restaurant.save()
                return Response({'message': 'Rating submitted successfully'})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
