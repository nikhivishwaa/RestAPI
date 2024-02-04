from rest_framework.viewsets import ModelViewSet
from .serializer import Student, StudentSerializer

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()