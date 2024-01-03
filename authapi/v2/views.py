from rest_framework.viewsets import ModelViewSet
from api.serializers import  Student, StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
