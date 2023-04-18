from django.db import models
from django.http import FileResponse

import os


class PDF(models.Model):
    filepath = os.path.join('static/', 'sample.pdf')
    file = FileResponse(open(filepath, 'rb'), content_type='application/pdf')