from django.shortcuts import render


def home(request):
    return render(request, 'davidvoong/home.html')

def pollupla(request):
    return render(request, 'davidvoong/pollupla.html')
