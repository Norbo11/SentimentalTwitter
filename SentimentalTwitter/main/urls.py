from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^home/', TemplateView.as_view(template_name="main/home.html")),
]