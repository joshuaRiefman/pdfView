import os

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FileSerializer
from .models import DisplayFile

# Create your views here.


def index(request):
    return HttpResponse("Hey!")


def get_pdf(request, file_name):
    filepath = os.path.join('static/', file_name)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


class FilesView(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = DisplayFile.objects.all()
