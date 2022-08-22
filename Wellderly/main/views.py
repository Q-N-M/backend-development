#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
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
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request):
        pass

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            response_data = {
                "status-code" : status.HTTP_401_UNAUTHORIZED,
                "description" : "Login failed",
            }
            return response.Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

        response_data = {
            "status-code" : status.HTTP_200_OK,
            "description" : "Login successful",
        }

        return response.Response(response_data, status=status.HTTP_200_OK)

class EmojiView(viewsets.ModelViewSet):
    queryset = Emoji.objects.all().order_by('id')
    serializer_class = EmojiSerializer
    permission_classes = [AllowAny]
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

class UserEmojiView(viewsets.ModelViewSet):
    queryset = UserEmoji.objects.all().order_by('id')
    serializer_class = UserEmojiSerializer
    permission_classes = [AllowAny]
    
    def list(self, request):
        total_data = UserEmoji.objects.all().count()
        json_data = {}
        for i in range(5):
            emoji_data = UserEmoji.objects.filter(emoji=i+1).count()
            json_data['emoji_'+str(i+1)+'_data'] = (emoji_data/total_data)*100
        return response.Response({'count_data':json_data})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
