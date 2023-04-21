from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from user.models import Employee
from .models import Restaurant
from .serializers import RestaurantSerializer, RestaurantListSerializer
from .views import RestaurantViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.test import APIClient
from django.urls import reverse


class RestaurantViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.restaurant = Restaurant.objects.create(name="Test Restaurant", address="Test Location")
        self.user = Employee.objects.create_user(email="testuser@mail.com", password="testpassword")

    def test_get_serializer_class_list_action(self):
        view = RestaurantViewSet()
        view.action = "list"
        serializer_class = view.get_serializer_class()
        self.assertEqual(serializer_class, RestaurantListSerializer)

    def test_get_serializer_class_other_actions(self):
        view = RestaurantViewSet()
        view.action = "create"
        serializer_class = view.get_serializer_class()
        self.assertEqual(serializer_class, RestaurantSerializer)

    def test_get_permissions_list_and_retrieve_actions(self):
        view = RestaurantViewSet()
        view.action = "list"
        permissions = view.get_permissions()
        self.assertTrue(any(isinstance(permission, AllowAny) for permission in permissions))

        view.action = "retrieve"
        permissions = view.get_permissions()
        self.assertTrue(any(isinstance(permission, AllowAny) for permission in permissions))

    def test_get_permissions_other_actions(self):
        view = RestaurantViewSet()
        view.action = "create"
        permissions = view.get_permissions()
        self.assertTrue(any(isinstance(permission, IsAuthenticated) for permission in permissions))


    def test_restaurant_list_viewset(self):
        view = RestaurantViewSet.as_view({"get": "list"})
        request = self.factory.get("/restaurants/")
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_restaurant_create_viewset_unauthenticated(self):
        view = RestaurantViewSet.as_view({"post": "create"})
        request = self.factory.post("/restaurants/", data={"name": "New Restaurant", "address": "New Location"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_restaurant_create_viewset_authenticated(self):
        view = RestaurantViewSet.as_view({"post": "create"})
        request = self.factory.post("/restaurants/", data={"name": "New Restaurant", "address": "New Location"})
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
