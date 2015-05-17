from django.db import models

class Scale(models.Model):
    key = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
