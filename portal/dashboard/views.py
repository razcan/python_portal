from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'dashboard_page.html')

def dashboard(request):
    return render(request, 'dashboard_page.html')
