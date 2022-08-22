from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from main.models import User
from main.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status, response

# Create your views here.

class UserChatViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]