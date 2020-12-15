from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import ComplaintsForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Complaints


def index(request):
    results = Complaints.objects.all()
    return render(request, 'complaints_page.html', {'results': results})


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


def edit(request, id):
    result = Complaints.objects.get(id=id)
    return render(request, 'edit.html', {'result': result})


def update(request, id):
    result = Complaints.objects.get(id=id)
    form = ComplaintsForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect("/complaints")
    return render(request, 'edit.html', {'result': result})

