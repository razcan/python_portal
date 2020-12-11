from django.contrib import admin
from .models import Complaints
from django import forms


class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at')
    list_per_page = 4
    list_filter = ('created_at',)


admin.site.register(Complaints, ComplaintsAdmin)
