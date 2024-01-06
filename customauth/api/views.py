from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer, Student


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
