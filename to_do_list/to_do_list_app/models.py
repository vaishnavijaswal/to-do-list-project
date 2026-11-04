from django.db import models


# Create your models here.
class task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  completed = models.BooleanField(default=False)
  created = models.DateField(auto_now_add=True)