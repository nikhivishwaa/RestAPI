from rest_framework import serializers
from .models import Student, Teacher, Worker

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__" 


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__" 


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__" 
    