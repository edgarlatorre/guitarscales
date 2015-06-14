from django.conf.urls import url
from scales.views import ScaleDetail

urlpatterns = [
    url(r'^(?P<slug>[-\w\d]+)/$', ScaleDetail.as_view(), name='scale-detail'),
]
