from api.serializers import Student, StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView


class StudentListAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateAPI(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveAPI(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateAPI(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDestroyAPI(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListCreateAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateAPI(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveDestroyAPI(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

   
class StudentRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer