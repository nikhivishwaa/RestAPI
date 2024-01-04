from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter
from .auth import CustomAuthToken



router = DefaultRouter()
router.register('students', views.StudentViewSet, basename="students")

urlpatterns = [
    path('',  include(router.urls)),
    path('register/', CustomAuthToken.as_view()),
]
