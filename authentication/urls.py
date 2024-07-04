from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path("welcome/", welcome_page, name='welcome'),
    path("logout/", logout_page, name='logout'),
]