from django.shortcuts import render
from django.http import HttpResponse


def recog(request):
    return HttpResponse("Hello world!")
