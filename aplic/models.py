from django.db import models
from stdimage.models import StdImageField
import uuid
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Curso(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=500)
    imagem = StdImageField(_('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
    carga_horaria = models.IntegerField(_('Carga Horária'))

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    foto = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField(_('Facebook'), blank=True, max_length=200)
    linkedin = models.CharField(_('LinkedIn'), blank=True, max_length=200)
    twitter = models.CharField(_('Twitter'), blank=True, max_length=200)
    instagram = models.CharField(_('Instagram'), blank=True, max_length=200)

    class Meta:
        abstract = True
        verbose_name = _('Professor')
        verbose_name_plural = _('Professores')

    def __str__(self):
        return self.nome


class Professor(Pessoa):
    OPCOES = (
        ('Doutorado',       _('Doutorado')),
        ('Mestrado',        _('Mestrado')),
        ('Especialização',  _('Especialização')),
        ('Graduação',       _('Graduação')),
    )
    titulacao = models.CharField(_('Titulação'), blank=True, max_length=100, choices=OPCOES)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL)
    curriculo = models.TextField(_('Currículo'), blank=True, max_length=500)

    class Meta:
        verbose_name = _('Professor')
        verbose_name_plural = _('Professores')


class Aluno(Pessoa):
    matricula = models.IntegerField(_('Matrícula'), unique=True)
    data_nascimento = models.DateField(_('Data de Nascimento'), blank=True, null=True, help_text=_('Formato DD/MM/AAAA'))
    email = models.EmailField(_('E-mail'), blank=True, max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Aluno')
        verbose_name_plural = _('Alunos')


class Disciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome = models.CharField(_('Nome'), max_length=100)
    carga_horaria = models.IntegerField(_('Carga horária'))
    obrigatoria = models.BooleanField(_('Obrigatória'), default=True)
    ementa = models.TextField(_('Ementa'), blank=True, max_length=500)
    bibliografia = models.TextField(_('Bibliografia'), blank=True, max_length=500)

    class Meta:
        verbose_name = _('Disciplina')
        verbose_name_plural = _('Disciplinas')

    def __str__(self):
        return self.nome


class Turma(models.Model):
    ano = models.IntegerField(_('Ano'))
    semestre = models.IntegerField(_('Semestre'))
    turma = models.CharField(_('Turma'), max_length=10)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)
    alunos = models.ManyToManyField(Aluno)

    class Meta:
        verbose_name = _('Turma')
        verbose_name_plural = _('Turmas')

    def __str__(self):
        return f"{self.ano} / {self.semestre} / {self.turma} / {self.disciplina}"

