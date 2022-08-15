#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import *
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class UserLoginView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        response = {
            "status-code" : status.HTTP_200_OK,
            "description" : "Login successful",
        }

        return Response(response, status=status.HTTP_200_OK)
