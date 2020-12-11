from .models import Complaints
from django.forms import ModelForm

class ComplaintsForm(ModelForm):
    class Meta:
        model = Complaints
        fields = '__all__'
