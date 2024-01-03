from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students', views.StudentViewSet, basename="students")

urlpatterns = [
    path('',  include(router.urls)),
    path("auth/", include('rest_framework.urls'))
]
