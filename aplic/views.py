from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class SobreView(TemplateView):
    template_name = 'about-us.html'
