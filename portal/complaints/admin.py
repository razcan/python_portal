from django.contrib import admin
from .models import Complaints
from django import forms


# class ComplaintsForm(forms.ModelForm):
#     class Meta:
#         model = Complaints
#         exclude = ['id']
#
#
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at')
    list_filter = ('created_at',)


admin.site.register(Complaints, ComplaintsAdmin)
