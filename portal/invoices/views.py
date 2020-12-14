from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'invoices_page.html')

def invoices(request):
    return render(request, 'invoices_page.html')

