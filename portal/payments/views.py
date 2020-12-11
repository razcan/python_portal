from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'payments_page.html')

def payments(request):
    return render(request, 'payments_page.html')
