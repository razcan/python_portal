from django.urls import path

from . import views

app_name = 'complaints'

urlpatterns = [
    path('index', views.index, name='index'),
    path('complaints', views.complaints, name='complaints'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]