from django.views.generic import DetailView
from django.http import HttpResponse
from scales.models import Scale

class ScaleDetail(DetailView):
    model = Scale
    template_name = 'scales/detail.html'
