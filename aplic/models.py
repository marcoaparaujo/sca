from django.db import models


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    carga_horaria = models.IntegerField('Carga Horária')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome


class Professor(models.Model):
    OPCOES = (
        ('Doutorado',       'Doutorado'),
        ('Mestrado',        'Mestrado'),
        ('Especialização',  'Especialização'),
        ('Graduação',       'Graduação'),
    )
    nome = models.CharField('Nome', max_length=100)
    titulacao = models.CharField('Titulação', blank=True, max_length=100, choices=OPCOES)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return self.nome
