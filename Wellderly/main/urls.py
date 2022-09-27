from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'login', UserLoginView, basename='login')
router.register(r'emoji', EmojiView, basename='emoji')
router.register(r'user-emoji', UserEmojiView, basename='user-emoji')
router.register(r'user-analysis', UserAnalysisView, basename='user-analysis')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
