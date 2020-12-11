from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import ComplaintsForm


def complaints(request):
    return render(request, 'complaints_page.html')


def index(request):
    form = ComplaintsForm()
    if request.method == 'POST':

        form = ComplaintsForm(request.POST)
        if form.is_valid():
            #print(request.POST)
            #print(form.cleaned_data["text"])
            form.save()
        #return HttpResponseRedirect("/invoices")
    context = {'form': form}
    return render(request, 'complaints_page.html', context)
