from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Тест на работоспособность кириллицы! <P>Hello, world. You're at the polls index.</P>")