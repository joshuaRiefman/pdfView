from django.urls import path
from . import views

urlpatterns = [
    path('<str:file_name>', views.show_pdf, name='show_pdf'),
    path('', views.index, name='index'),
]
