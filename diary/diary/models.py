# diary/models.py

from django.db import models

class DiaryEntry(models.Model):
    file_name = models.CharField(max_length=255)
    date = models.DateField()
    text = models.TextField()

class Meta:
        app_label = 'diary'