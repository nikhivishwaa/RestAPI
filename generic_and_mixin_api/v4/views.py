from api.serializers import Student, StudentSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status


class StudentViewSet(ViewSet):
    def list(self, request):
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data)

    def create(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=status.HTTP_201_CREATED)
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            student = Student.objects.get(pk = pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Exception as e:
            res = {"detail": "Not found."}
            return Response(res, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        try:
            student = Student.objects.get(pk = pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            res = {"detail": "Not found."}
            return Response(res, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk):
        try:
            student = Student.objects.get(pk = pk)
            serializer = StudentSerializer(student, data=request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            res = {"detail": "Not found."}
            return Response(res, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            student = Student.objects.get(pk = pk)
            student.delete()
            return Response({"student": "deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            res = {"detail": "Not found."}
            return Response(res, status=status.HTTP_404_NOT_FOUND)