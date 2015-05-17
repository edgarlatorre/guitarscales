from django.db import models

class Scale(models.Model):
    key = models.CharField(max_length=2)
    name = models.CharField(max_length=30)

    def __str__(self):
        return u"%s %s" % (self.key, self.name)

class Shape(models.Model):
    number = models.IntegerField()
    first_fret = models.IntegerField()
    scale = models.ForeignKey(Scale)

    def __str__(self):
        return u"%s %s" % (str(self.scale), self.number)

class Position(models.Model):
    fret = models.IntegerField()
    string = models.IntegerField()
    finger = models.IntegerField()
    is_root = models.BooleanField()
    shape = models.ForeignKey(Shape)

    def __str__(self):
        return u"%s Position: %d : %d" % (str(self.shape),
            self.fret, self.string)
