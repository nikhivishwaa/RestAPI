from django.urls import path
from . import views 

urlpatterns = [
    path('students/',  views.StudentListCreateAPI.as_view()),
    path('students/<int:pk>/',  views.StudentRUDAPI.as_view()),
]
