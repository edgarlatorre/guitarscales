from django.test import TestCase
from scales.models import Scale, Shape, Position

class ScaleTest(TestCase):
    def test_scale__representation(self):
        scale = Scale()
        scale.key = "E"
        scale.name = "Minor Pentatonic"

        self.assertEquals("%s %s" % (scale.key, scale.name), str(scale))

class ShapeTest(TestCase):
    def setUp(self):
        self.scale = Scale()
        self.scale.key = "E"
        self.scale.name = "Minor Pentatonic"
        self.scale.save()

    def tearDown(self):
        Scale.objects.all().delete()

    def test_shape_string_representation(self):
        shape = Shape()
        shape.number = 1
        shape.scale = self.scale

        self.assertEquals("%s %s" % (str(self.scale), shape.number), str(shape))

class PositionTest(TestCase):
    def setUp(self):
        self.scale = Scale()
        self.scale.key = "E"
        self.scale.name = "Minor Pentatonic"
        self.scale.save()

        self.shape = Shape()
        self.shape.number = 1
        self.shape.first_fret = 1
        self.shape.scale = self.scale
        self.shape.save()

    def tearDown(self):
        Scale.objects.all().delete()
        Shape.objects.all().delete()

    def test_shape_string_representation(self):
        position = Position()
        position.fret = 1
        position.string = 2
        position.shape = self.shape

        expected = "%s Position: %d : %d" % (str(self.shape),
            position.fret, position.string)

        self.assertEquals(expected, str(position))
