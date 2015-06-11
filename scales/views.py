from django.views.generic import DetailView
from django.http import HttpResponse
from scales.models import Scale

class ScaleDetail(DetailView):
    model = Scale
    template_name = 'scales/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ScaleDetail, self).get_context_data(**kwargs)

        scale = Scale.objects.get(pk=2)
        necks = []

        for shape in scale.shape_set.all():
            neck = [[0 for x in range(15)] for x in range(6)]

            for position in shape.position_set.all():
                neck[position.string - 1][position.fret - 1] = position

            necks.append(neck)

        context['necks'] = necks

        return context
