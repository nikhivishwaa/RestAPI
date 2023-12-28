from rest_framework.serializers import HyperlinkedModelSerializer, ReadOnlyField
from .models import Company, Employee


class CompanySerializer(HyperlinkedModelSerializer):
    # company_id = ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"   # seraialize all fields


class EmployeeSerializer(HyperlinkedModelSerializer):
    emp_id = ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"
