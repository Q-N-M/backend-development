#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import *
from .models import User
from rest_framework.permissions import AllowAny
from rest_framework import status, response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return response.Response({'message': 'kennot'}, status=status.HTTP_400_BAD_REQUEST)


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
