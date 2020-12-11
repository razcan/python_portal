from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('invoices/', include('invoices.urls')),
    path('payments/', include('payments.urls')),
    path('admin/', admin.site.urls),
    path('', include('invoices.urls')),
]
