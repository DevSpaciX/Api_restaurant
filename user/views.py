import random

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        versions = ["3.11","10.3"]
        response.data['custom-header'] = {
            'app_version': random.choice(versions),
        }
        return response


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

