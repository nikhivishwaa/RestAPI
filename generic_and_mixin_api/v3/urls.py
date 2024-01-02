from django.urls import path
from . import views 

urlpatterns = [
    # path('students/',  views.StudentCreateAPI.as_view()),
    # path('students/',  views.StudentListAPI.as_view()),
    # path('students/<int:pk>/',  views.StudentDestroyAPI.as_view()),
    # path('students/<int:pk>/',  views.StudentUpdateAPI.as_view()),
    # path('students/<int:pk>/',  views.StudentRetrieveAPI.as_view()),
    
    path('students/',  views.StudentListCreateAPI.as_view()),
    # path('students/<int:pk>/',  views.StudentRetrieveUpdateAPI.as_view()),
    # path('students/<int:pk>/',  views.StudentRetrieveDestroyAPI.as_view()),
    path('students/<int:pk>/',  views.StudentRetrieveUpdateDestroyAPI.as_view()),
]
