from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students', views.StudentViewSet, basename="students")

urlpatterns = [
    path('',  include(router.urls)),
    path('v1/',  include('v1.urls')),
    path('v2/',  include('v2.urls')),
    path('v3/',  include('v3.urls')),
]
