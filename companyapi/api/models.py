from django.db import models

typeofcompany = (('IT', "IT"),
                 ('Non IT', "Non IT"),
                 ('Retail', "Retail"))

typeofemp = (('Manager', "manager"),
             ('Software Developer', "sd"),
             ('Project Leader', "pl"))


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=typeofcompany)
    about = models.TextField()
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    type = models.CharField(max_length=25, choices=typeofemp)
    location = models.CharField(max_length=200)
    joining_date = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
