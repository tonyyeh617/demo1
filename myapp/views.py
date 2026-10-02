from django.shortcuts import render
from django.http import HttpResponse

def aweb(request):
    return HttpResponse("Hello, this is aweb view.完成")

def bweb(request):
    return HttpResponse("Hello, this is the bweb view.完成!")