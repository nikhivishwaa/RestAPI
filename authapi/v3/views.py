from rest_framework.viewsets import ModelViewSet
from api.serializers import  Student, StudentSerializer
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
