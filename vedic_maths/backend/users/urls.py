from django.urls import path, include
from .api import RegisterAPI, signIn
from rest_framework import routers

router = routers.DefaultRouter()
router.register('signup', RegisterAPI, 'signup')


urlpatterns = [
    path('', include(router.urls)),
    path('login', signIn)
    
]
