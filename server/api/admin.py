from django.contrib import admin
from .models import DisplayFile

# Register your models here.


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(DisplayFile, FileAdmin)
