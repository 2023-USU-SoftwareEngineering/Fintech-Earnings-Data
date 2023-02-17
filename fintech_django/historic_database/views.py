from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Django gets cranky with relative imports.
# At some point I should pull the ..sql_functions.py file into this directory so pycharm doesn't throw errors either
from sql_functions import get_companies, get_history
from datetime import datetime
import json


def index(request):
    return render(request, 'historic_database/index.html')


def pull(request):
    company_str = request.GET.get('company')
    from_str = request.GET.get('from')
    to_str = request.GET.get('to')
    if company_str is None or from_str is None or to_str is None:
        data = {
            'error': 'Invalid request. See usage'
        }
        return JsonResponse(data)

    from_str = from_str.replace('.', '/')
    from_date = datetime.strptime(from_str, '%Y/%m/%d')
    to_str = from_str.replace('.', '/')
    to_date = datetime.strptime(to_str, '%Y/%m/%d')
    # TODO: convert dates to numerical value. Ask Rett

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

    # TODO: make API communicate with sqlite database
    # history = json.loads(get_history(from_date, to_date, company_str))
    history = {
        'company': company_str,
        'from': from_date,
        'to': to_date,
        'history': 'Test response. Actual data pull to be implemented',
    }
    return JsonResponse(history)
