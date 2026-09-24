from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def aweb(request):
    return HttpResponse("Hello, this is the aweb view.")