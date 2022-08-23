from django.shortcuts import render
from rest_framework import generics
from .models import UserAccount
from .serializers import UserCreateSerializers

class CreateUser(generics.CreateAPIView):
    
    queryset = UserAccount
    serializer_class = UserCreateSerializers