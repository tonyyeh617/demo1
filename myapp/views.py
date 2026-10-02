from django.shortcuts import render
from django.http import HttpResponse

def aweb(request):
    return HttpResponse("Hello, this is aweb view.")
