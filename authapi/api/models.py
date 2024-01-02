from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=30)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=25)
    city = models.CharField(max_length=30)


class Worker(models.Model):
    name = models.CharField(max_length=50)
    workerid = models.IntegerField()
    city = models.CharField(max_length=30)

