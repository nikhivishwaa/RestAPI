from rest_framework.viewsets import ModelViewSet
from api.serializers import StudentSerializer, Student


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
