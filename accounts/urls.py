from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register
urlpatterns=[

path('',home),
path('register/',register),
]
