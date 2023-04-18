from django.http import FileResponse
from django.shortcuts import render
import os


def show_pdf(request, file_name):
    filepath = os.path.join('static/', file_name)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def index(request):
    return render(request, template_name='viewer/index.html')
