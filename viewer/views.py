from django.http import FileResponse
import os


def show_pdf(request, file_name):
    filepath = os.path.join('static/', file_name)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
