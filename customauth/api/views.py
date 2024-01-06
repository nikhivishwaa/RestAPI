from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer, Student
from .customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
