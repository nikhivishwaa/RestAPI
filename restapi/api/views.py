from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
import json


def student(request):
    print(request, type(request))
    print(request.method,type(request.method))
    print(request.body, type(request.body))
    print(request.GET, type(request.GET))
    stream = io.BytesIO(request.body)
    print(stream, type(stream))
    py_data = JSONParser().parse(stream)
    print(py_data, type(py_data))
    print(json.dumps(py_data), type(json.dumps(py_data)))
    print(py_data, type(py_data))
    
    return JsonResponse({'message': 'success', 'yes': 'yes'})