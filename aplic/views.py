from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Professor, Curso, Disciplina


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.order_by('?').all()
        return context


class SobreView(TemplateView):
    template_name = 'about-us.html'


class ProfessoresView(TemplateView):
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super(ProfessoresView, self).get_context_data(**kwargs)
        context['professores'] = Professor.objects.order_by('nome').all()
        return context


class CursoDetalheView(ListView):
    template_name = 'course-detail.html'
    paginate_by = 5
    ordering = 'nome'
    model = Disciplina

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Disciplina.objects.filter(curso_id=id)

