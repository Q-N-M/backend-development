#from django.shortcuts import render
from asyncio import current_task
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
from rest_framework import status, response
from datetime import date, timedelta
from django.core import serializers
from django.http import HttpResponse
import json

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

    def create(self, request):
        updated_request = request.POST.copy()
        current_time = date.today()
        updated_request.update({'date':current_time})
        serializer = self.serializer_class(data=updated_request)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAnalysisView(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserEmojiSerializer

    def list(self, request):
        #total_data = UserEmoji.objects.all().order_by('date')
        #json_data = {}
        #for i in range(5):
        #    emoji_data = UserEmoji.objects.filter(emoji=i+1).count()
        #    json_data['emoji_'+str(i+1)+'_data'] = (emoji_data/total_data)*100
        #return response.Response({'count_data':json_data})
        
        
        distinct_date = UserEmoji.objects.all().distinct('date').order_by('-date')
        date_total = len(distinct_date)
        list_data = {}
        for i in range(date_total):
            object_data = {"emoji_1_data":0,"emoji_2_data":0,"emoji_3_data":0,"emoji_4_data":0,"emoji_5_data":0,}
            current_date = distinct_date[i].date
            total_data_count = UserEmoji.objects.filter(date=current_date).count()
            for j in range(5):
                emoji_data = UserEmoji.objects.filter(date=current_date,emoji=j+1).count()
                emoji_percentage = (emoji_data/total_data_count)*100
                percentage_fix = "{:.2f}".format(emoji_percentage)
                object_data.update({'emoji_'+str(j+1)+'_data':[percentage_fix,emoji_data]})
            object_data.update({'total_data':total_data_count})
            list_data.update({str(current_date):object_data})
        json_data = json.dumps(list_data)
        
        

        return HttpResponse(json_data, content_type='application/json')

    def create(self, request):
        pass