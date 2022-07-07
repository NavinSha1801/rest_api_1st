from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('rest-auth/',include('rest_auth.urls')),
    path('',secondview.as_view(),name='get_method'),
    path('create/',PostCreateView.as_view(), name = 'post_method')
]