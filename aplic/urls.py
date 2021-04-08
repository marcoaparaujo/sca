from django.urls import path

from .views import IndexView, SobreView, ProfessoresView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('professores/', ProfessoresView.as_view(), name='professores'),

]
