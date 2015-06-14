from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from scales.models import Scale

class ScaleDetail(DetailView):
    model = Scale
    template_name = 'scales/detail.html'

    def get_object(self):
        return get_object_or_404(Scale, slug=self.kwargs.get('slug', None))
