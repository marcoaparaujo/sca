from django.views.generic import TemplateView

from .models import Professor

class IndexView(TemplateView):
    template_name = 'index.html'


class SobreView(TemplateView):
    template_name = 'about-us.html'


class ProfessoresView(TemplateView):
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super(ProfessoresView, self).get_context_data(**kwargs)
        context['professores'] = Professor.objects.order_by('?').all()
        return context

