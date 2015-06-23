from django.views.generic import TemplateView
from scales.models import Scale

class IndexView(TemplateView):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["scales"] = Scale.objects.all()
        return self.render_to_response(context)
