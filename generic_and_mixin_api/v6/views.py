from rest_framework.viewsets import ReadOnlyModelViewSet
from api.serializers import StudentSerializer, Student


class StudentReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
