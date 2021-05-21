from rest_framework import serializers

from aplic.models import Curso, Aluno, Disciplina, Professor


class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplina
        fields = (
            'id',
            'nome',
            'curso'
        )


class CursoSerializer(serializers.ModelSerializer):
    disciplinas = DisciplinaSerializer(many=True, read_only=True)
    # disciplinas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # disciplinas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='disciplina-detail')

    class Meta:
        model = Curso
        fields = (
            'id',
            'nome',
            'descricao',
            'imagem',
            'carga_horaria',
            'disciplinas'
        )


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = (
            'id',
            'matricula',
            'data_nascimento',
            'email',
            'nome',
            'curso'
        )


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = (
            'id',
            'nome',
            'titulacao',
            'curso'
        )

