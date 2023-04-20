from django.urls import path, include
from rest_framework.routers import SimpleRouter
from restaurant.views import RestaurantViewSet, MenuViewSet

router = SimpleRouter()
router.register("restaurants", RestaurantViewSet, basename="restaurants")
router.register("menu", MenuViewSet, basename="menu")
urlpatterns = [
    path("", include(router.urls)),
]

app_name = "restaurants-endpoint"
