from rest_framework.viewsets import ModelViewSet
from api import serializers as sr
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


class StudentViewSet(ModelViewSet):
    queryset = sr.Student.objects.all()
    serializer_class = sr.StudentSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser, IsAuthenticated]


class TeacherViewSet(ModelViewSet):
    queryset = sr.Teacher.objects.all()
    serializer_class = sr.TeacherSerializer


class WorkerViewSet(ModelViewSet):
    queryset = sr.Worker.objects.all()
    serializer_class = sr.WorkerSerializer
