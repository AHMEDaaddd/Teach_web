from django.urls import path
from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserProfileUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

urlpatterns = [
    path("users/<int:pk>/", UserProfileUpdateAPIView.as_view(), name="user-profile-update"),
]