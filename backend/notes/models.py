from django.db import models

# Create your models here.

class Note(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField()
  addition = models.TextField(default='')
  created_at = models.DateTimeField(auto_now_add=True)