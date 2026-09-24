from django.shortcuts import render

from django.http import HttpResponse

def bweb(request):
    return HttpResponse("Hello, this is the bweb view. 完成")
