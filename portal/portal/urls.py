from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('invoices/', include('invoices.urls')),
    path('complaints/', include('complaints.urls')),
    path('payments/', include('payments.urls')),
    path('admin/', admin.site.urls),
    path('', include('invoices.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
