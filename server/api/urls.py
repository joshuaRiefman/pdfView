from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:file_name>", views.get_pdf, name='get_pdf')
]