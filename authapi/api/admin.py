from django.contrib import admin
from .models import Student, Teacher, Worker


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'city']


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'workerid', 'city']
