
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('ticket/', ticket_view, name='ticket'),
    path('login/', login, name='login'),

]
