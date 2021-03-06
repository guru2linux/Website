import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home():
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
            }
    )