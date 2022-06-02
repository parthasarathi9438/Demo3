from django.shortcuts import render
from app3.models import Profile
from django.contrib.auth.models import User
from app3.serializers import ProfileSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class Profile(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class UserOperation(ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
