from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello world")