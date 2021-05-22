from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import IndexView, SobreView, ProfessoresView, CursoDetalheView, DadosGraficoAlunosView, RelatorioAlunosView, \
    ContatoView, CursoViewSet, AlunoViewSet, DisciplinaViewSet, ProfessorViewSet, TurmaViewSet

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('alunos', AlunoViewSet)
router.register('disciplinas', DisciplinaViewSet)
router.register('professores', ProfessorViewSet)
router.register('turmas', TurmaViewSet)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('professores/', ProfessoresView.as_view(), name='professores'),
    path('curso-detalhe/<int:id>/', CursoDetalheView.as_view(), name='curso-detalhe'),
    path('dados-grafico-alunos/', DadosGraficoAlunosView.as_view(), name='dados-grafico-alunos'),
    path('relatorio-alunos/', RelatorioAlunosView.as_view(), name='relatorio-alunos'),
]
