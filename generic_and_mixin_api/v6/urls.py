from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students', views.StudentReadOnlyModelViewSet, basename="students")

urlpatterns = [
    path('',  include(router.urls)),
]
