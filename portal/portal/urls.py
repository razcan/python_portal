from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import url


urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('invoices/', include('invoices.urls')),
    path('complaints/', include('complaints.urls')),
    path('payments/', include('payments.urls')),
    path('admin/', admin.site.urls),
    url(r'^dashboard/$', views.dashboard),
    url(r'^invoices/$', views.invoices),
    url(r'^complaints/$', views.complaints),
    path('', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
