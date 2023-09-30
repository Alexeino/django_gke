from django.shortcuts import render, HttpResponse
# Create your views here.

def ok(request):
    
    return HttpResponse("OK")