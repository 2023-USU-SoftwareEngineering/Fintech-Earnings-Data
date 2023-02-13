from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def index(request):
    return render(request, 'historic_database/index.html')


def pull(request):
    data = {
        "test": "test response"
    }
    return JsonResponse(data)
