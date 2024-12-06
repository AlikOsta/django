from django.shortcuts import render
from django.http import HttpResponse
from . import models



def index(request, name):
    string = f'Привет {name}'
    return HttpResponse(string)