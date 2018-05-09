from django.db import models
from datetime import datetime

# Create your models here.
class Form(models.Model):
    file_path = models.FileField(upload_to='files/')
    form_name = models.CharField(max_length=255, null=True)
    form_instruction = models.TextField(null=True)
    form_notes = models.TextField(null=True)
    upload_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.form_name
