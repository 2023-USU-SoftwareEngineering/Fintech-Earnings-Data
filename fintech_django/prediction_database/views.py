from django.shortcuts import render
from django.http import JsonResponse
# Django gets cranky with relative imports.
# At some point I should pull the ..sql_functions.py file into this directory so pycharm doesn't throw errors either
from sql_functions import get_companies, get_prediction
import json


def index(request):
    return render(request, 'prediction_database/index.html')


def pull(request):
    company_str = request.GET.get('company')
    if company_str is None:
        data = {
            'error': 'Invalid request. See usage'
        }
        return JsonResponse(data)

    companies = get_companies()
    companies = json.loads(companies)
    company_exists = False
    for company in companies['info']:
        # "company" is still a list, name is at index 0
        if company[0] == company_str:
            company_exists = True
    if not company_exists:
        data = {
            'error': 'Company name is invalid.'
        }
        return JsonResponse(data)

    prediction = json.loads(get_prediction(company_str))
    response = {
        'company': company_str,
        'prediction': prediction,
    }
    return JsonResponse(response)


