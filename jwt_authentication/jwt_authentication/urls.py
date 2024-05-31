
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path("gettoken/", TokenObtainPairView.as_view(), name='generate_token'),
    path("refreshtoken/", TokenRefreshView.as_view(), name='refresh_token'),
    path("verifytoken/", TokenVerifyView.as_view(), name='verify_token')
]
