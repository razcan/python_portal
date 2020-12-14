from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'base1.html')

def dashboard(request):
    return HttpResponse('dashboard')


def invoices(request):
    return HttpResponse('invoices')


def complaints(request):
    return HttpResponse('complaints')
