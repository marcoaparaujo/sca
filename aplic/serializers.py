from rest_framework import serializers

from aplic.models import Curso, Aluno, Disciplina, Professor, Turma


class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplina
        fields = (
            'id',
            'nome',
            'curso'
        )


class CursoSerializer(serializers.ModelSerializer):
    # disciplinas = DisciplinaSerializer(many=True, read_only=True)
    # disciplinas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    disciplinas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='disciplina-detail')

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

    def validate_carga_horaria(self, valor):
        if valor >= 20:
            return valor
        raise serializers.ValidationError('Carga Horária inválida')



class AlunoSerializer(serializers.ModelSerializer):

    primeiro_nome = serializers.SerializerMethodField()

    class Meta:
        model = Aluno
        fields = (
            'id',
            'matricula',
            'data_nascimento',
            'email',
            'nome',
            'curso',
            'primeiro_nome'
        )

    def get_primeiro_nome(self, obj):
        return str(obj.nome).split()[0]


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = (
            'id',
            'nome',
            'titulacao',
            'curso'
        )


class TurmaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Turma
        fields = (
            'id',
            'ano',
            'semestre',
            'turma',
            'disciplina',
            'professor'
        )
