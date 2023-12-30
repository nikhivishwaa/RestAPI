from django.contrib import admin
from django.urls import path, include
from .views import StudenAPI

urlpatterns = [
    path('students/',  StudenAPI.as_view()),
]
