from rest_framework import serializers
from rest_framework import viewsets
from restaurant.models import Restaurant, Menu


class MenuSerializer(serializers.ModelSerializer):
    daily_menu = serializers.ChoiceField(choices=Menu.DAYS_OF_WEEK_CHOICES)

    class Meta:
        model = Menu
        fields = ["drink", "main_dish", "dessert", "daily_menu", "restaurant"]


class MenuForRestaurantSerializer(MenuSerializer):
    daily_menu = serializers.CharField(source="get_daily_menu_display")


class MenuListSerializer(MenuSerializer):
    restaurant = serializers.SerializerMethodField()
    daily_menu = serializers.CharField(source="get_daily_menu_display")

    def get_restaurant(self, obj):
        if obj.restaurant:
            return obj.restaurant.name
        return None

    class Meta:
        model = Menu
        fields = [
            "drink",
            "main_dish",
            "dessert",
            "daily_menu",
            "restaurant",
            "daily_menu",
            "price",
        ]


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["name", "address"]


class RestaurantListSerializer(serializers.ModelSerializer):
    menu = MenuForRestaurantSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ["name", "address", "menu"]


class VoteListSerializer(MenuSerializer):
    restaurant = serializers.SerializerMethodField()
    daily_menu = serializers.CharField(source="get_daily_menu_display")
    vote = serializers.IntegerField(source="restaurant.votes")

    def get_restaurant(self, obj):
        if obj.restaurant:
            return obj.restaurant.name
        return None

    class Meta:
        model = Menu
        fields = ["restaurant", "vote", "drink", "main_dish", "dessert", "price"]


class VoteSerializer(MenuSerializer):
    vote = serializers.IntegerField()

    class Meta:
        model = Menu
        fields = ["restaurant", "vote"]
