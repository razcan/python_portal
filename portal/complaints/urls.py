from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complaints', views.complaints, name='complaints'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
]