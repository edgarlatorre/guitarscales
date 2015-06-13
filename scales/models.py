from django.db import models
from django.utils.text import slugify

class Scale(models.Model):
    key = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify("{0}-{1}".format(self.key, self.name))
        if not(Scale.objects.filter(slug=self.slug)):
            super(Scale, self).save(*args, **kwargs)

    def __str__(self):
        return u"%s %s" % (self.key, self.name)

class Shape(models.Model):
    number = models.IntegerField()
    first_fret = models.IntegerField()
    scale = models.ForeignKey(Scale)

    def to_table(self):
        table = [[None for x in range(16)] for x in range(6)]

        for position in self.position_set.all():
            table[position.string - 1][position.fret - 1] = position

        return table


    def __str__(self):
        return u"%s %s" % (str(self.scale), self.number)

class Position(models.Model):
    fret = models.IntegerField()
    string = models.IntegerField()
    finger = models.IntegerField()
    is_root = models.BooleanField()
    shape = models.ForeignKey(Shape)

    def get_css_class(self):
        if self.is_root:
            return 'root'

        return 'note'

    def __str__(self):
        return u"%s Position: %d : %d" % (str(self.shape),
            self.fret, self.string)

    class Meta:
        ordering = ["string","fret"]

# class NeckCreator(object):
#     @staticmethod
#     def draw(shapes):
#         for shape in shapes:
#             shapes_arr = []
#             strings = []
#             for string in range(1, 7):
#                 positions = []
#
#                 for fret in range(1, 15):
#                     for position in shape.position_set.all():
#
#
#                 strings[string] = positions
