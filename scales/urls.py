from django.conf.urls import url
from scales.views import ScaleDetail

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', ScaleDetail.as_view(), name='scale-detail'),
]
