from django.db import models

class Scale(models.Model):
    key = models.CharField(max_length=2)
    name = models.CharField(max_length=30)

class Shape(models.Model):
    number = models.IntegerField()
    first_fret = models.IntegerField()
    scale = models.ForeignKey(Scale)

class Position(models.Model):
    fret = models.IntegerField()
    string = models.IntegerField()
    finger = models.IntegerField()
    is_root = models.BooleanField()
    shape = models.ForeignKey(Shape)
