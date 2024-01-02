from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students', views.StudentViewSet, basename="students")
router.register('teachers', views.TeacherViewSet, basename="teachers")
router.register('workers', views.WorkerViewSet, basename="workers")

urlpatterns = [
    path('',  include(router.urls)),
]
