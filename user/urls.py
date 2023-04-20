from django.urls import path
from user.views import CreateUserView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("registration/",CreateUserView.as_view(),name="create-user"),
    path("login/", views.obtain_auth_token, name="token"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"