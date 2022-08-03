from django.http import HttpResponse
from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
def index(request):
   
    return JsonResponse({"result": [
        {"name": "kursjs"},
        {"name": "kursjs1"},
        {"name": "kursjs2"},
        {"name": "kursjs3"},
        {"name": "kursjs4"},
        {"name": "kursjs5"},
        {"name": "kursjs6"},
        {"name": "kursjs7"},
        {"name": "kursjs8"},
        {"name": "kursjs9"},
        {"name": "kursjs20"},     
    ]})
    