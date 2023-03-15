from django.shortcuts import render
from django.http import JsonResponse
from sql_functions import get_companies, get_history
import json


def index(request):
    return render(request, 'get_companies/index.html')


def list_companies(request):
    companies = get_companies()
    companies = json.loads(companies)
    return JsonResponse(companies)

