from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jampandu(request):
    return HttpResponse('Hi Jigelrani How are you!!')


def jigelrani(request):
    return HttpResponse('hello jampandu Iam fine')