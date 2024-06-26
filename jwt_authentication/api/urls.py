from django.urls import path,include
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("students",StudentViewSet, basename='students')

urlpatterns = [
    path("", include(router.urls))
]
