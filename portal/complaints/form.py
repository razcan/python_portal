from .models import Complaints
from django.forms import ModelForm
from django import forms


class ComplaintsForm(ModelForm):
    class Meta:
        model = Complaints
        fields = '__all__'


widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
           'text': forms.EmailInput(attrs={'class': 'form-control'}),
           'created_at': forms.TextInput(attrs={'class': 'form-control'}),
           }
