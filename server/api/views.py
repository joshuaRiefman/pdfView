from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FileSerializer
from .models import DisplayFile

# Create your views here.


def index(request):
    return HttpResponse("Hey!")


class FilesView(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = DisplayFile.objects.all()
