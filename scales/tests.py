from django.test import TestCase
from django.test import Client
from scales.models import Scale, Shape, Position
from scales.views import ScaleDetail

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
        
        self.shape = Shape()
        self.shape.number = 1
        self.shape.first_fret = 1
        self.shape.scale = self.scale
        self.shape.save()

    def tearDown(self):
        Scale.objects.all().delete()
        Shape.objects.all().delete()
        Position.objects.all().delete()

    def test_shape_string_representation(self):
        self.assertEquals("%s %s" % (str(self.scale), self.shape.number), str(self.shape))

    def test_to_table_length(self):
        self.assertEquals(6, len(self.shape.to_table()))

    def test_to_table_fret_length(self):
        self.assertEquals(16, len(self.shape.to_table()[0]))


    def test_to_table_default_values(self):
        expected = [
            [None for i in range(16)],
            [None for i in range(16)],
            [None for i in range(16)],
            [None for i in range(16)],
            [None for i in range(16)],
            [None for i in range(16)]
        ]

        self.assertEquals(expected, self.shape.to_table())
        
    def test_to_table_fret_default_values(self):
        self.assertEquals([None for i in range(16)], self.shape.to_table()[0])

    def test_to_table_with_position_on_string_one_fret_one(self):
        position = Position()
        position.fret = 1
        position.string = 1
        position.finger = 1
        position.is_root = True
        position.shape = self.shape
        position.save()
        
        self.assertEquals(position, self.shape.to_table()[0][0])




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
        
        self.position = Position()

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
    
    def test_get_css_class_returns_root(self):
        self.position.is_root = True;
        self.assertEquals('root', self.position.get_css_class())

    def test_get_css_class_returns_note(self):
        self.position.is_root = False
        self.assertEquals('note', self.position.get_css_class())


class ScaleDetail(TestCase):
    def setUp(self):
        self.client = Client()
        self.scale = Scale()
        self.scale.name = "Pentatonic"
        self.scale.key = "E"
        self.scale.save()

    def test_detail_return_200(self):
        response = self.client.get('/scales/{0}/'.format(self.scale.id))
        self.assertEquals(200, response.status_code)

    def test_detail_template(self):
        response = self.client.get('/scales/{0}/'.format(self.scale.id))
        self.assertTemplateUsed(response, 'scales/detail.html')

    def test_detail_return_404(self):
        response = self.client.get('/scales/0/')
        self.assertEquals(404, response.status_code)

