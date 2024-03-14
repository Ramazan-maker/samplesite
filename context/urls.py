
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('main/', index, name='index'),
    path('ticket/', ticket_view, name='ticket'),
]
