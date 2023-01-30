from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'adjective': "awesome"}
    return render(request, 'earnings_data/index.html', context)

