# myapp/models.py
from django.db import models

class TextFileContent(models.Model):
    content = models.TextField(default='')

    def __str__(self):
        return self.content