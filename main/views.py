from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/index.html', status=200)


def chat(request):
    return render(request, 'main/index-chat.html', status=200)
