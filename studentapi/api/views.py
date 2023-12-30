from django.http import JsonResponse, HttpResponse
from .models import Student
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer


@method_decorator(csrf_exempt, name='dispatch')
class StudenAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        try:
            datadict = JSONParser().parse(stream)
            id = datadict.get('id', None)
            if id is not None:
                try:
                    student = Student.objects.get(id=id)
                    serializer = StudentSerializer(student)
                    json_data = JSONRenderer().render(serializer.data)
                    return HttpResponse(json_data, content_type='application/json')
                except Exception as e:
                    return JsonResponse({'message': 'invalid id'})
        except Exception as e:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        datadict = JSONParser().parse(stream)
        serializer = StudentSerializer(data=datadict)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "data added successfully"})

        return JsonResponse(serializer.errors, safe=False)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        datadict = JSONParser().parse(stream)
        id = datadict.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(
                student, data=datadict, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "data updateded successfully"})

            return JsonResponse(serializer.errors, safe=False)
        return JsonResponse({"message": "id is missing"})

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        try:
            datadict = JSONParser().parse(stream)
            id = datadict.get('id', None)
            if id is not None:
                student = Student.objects.get(id=id)
                student.delete()
                return JsonResponse({"message": "item deleted"})
        except Exception as e:
            return JsonResponse({"message": "id is missing"})
