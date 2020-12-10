from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('invoices/', include('invoices.urls')),
    path('admin/', admin.site.urls),
]