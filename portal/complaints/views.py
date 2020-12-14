from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import ComplaintsForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'complaints_page.html')


def complaints(request):
    form = ComplaintsForm()
    if request.method == 'POST':

        form = ComplaintsForm(request.POST, request.FILES)
        if form.is_valid():
            #print(request.POST)
            #print(form.cleaned_data["text"])
            form.save()
            return redirect('dashboard')
        #return HttpResponseRedirect("/invoices")
    context = {'form': form}
    return render(request, 'complaints_page.html', context)
