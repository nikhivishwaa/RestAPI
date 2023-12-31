from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorAPIView.as_view()),
    path('vendors/<str:vc>/', views.VendorAPIView.as_view()),
]