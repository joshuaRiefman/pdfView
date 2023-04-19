from rest_framework import serializers
from .models import DisplayFile


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayFile
        fields = ('id', 'title', 'description')
