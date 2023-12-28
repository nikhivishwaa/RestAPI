from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # custom api ( ... /companies/{company_id}/employees)
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(emps,
                                                many=True,
                                                context={"request": request}
                                                )
            return Response(emp_serializer.data)

        except Exception as e:
            return Response({
                'message': 'this company might not exist !error'
            })


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
