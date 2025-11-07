from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def sample (request):
    return HttpResponse("Hello")
def sampleinfo (request):
    data ={"result":[1,2,3]}
    return JsonResponse(data)
def hello (request):
    return HttpResponse("Happy birthday OG")


