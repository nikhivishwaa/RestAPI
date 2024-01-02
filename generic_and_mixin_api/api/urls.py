from django.urls import path, include
from . import views 

urlpatterns = [
    path('students/',  views.StudentListView.as_view()),
    path('students/',  views.StudentCreateView.as_view()),
    path('students/<int:pk>/',  views.StudentDetailView.as_view()),
    path('students/<int:pk>/',  views.StudentUpdateView.as_view()),
    path('students/<int:pk>/',  views.StudentDestroyView.as_view()),
    path('v2/',  include('v2.urls')),
    path('v3/',  include('v3.urls')),
    path('v4/',  include('v4.urls')),
    path('v5/',  include('v5.urls')),
    path('v6/',  include('v6.urls')),
]
