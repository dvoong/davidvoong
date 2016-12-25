from django.shortcuts import render


def home(request):
    return render(request, 'davidvoong/home.html')

def pollupla(request):
    return render(request, 'davidvoong/pollupla.html')

def commonplace(request):
    return render(request, 'davidvoong/commonplace.html')

def cbt(request):
    return render(request, 'davidvoong/cbt.html')
