from django import forms
from .models import Agendamento, CaCursos, Curso

class CaCursosForm(forms.ModelForm):
    class Meta:
        model = CaCursos
        fields = ['nome', 'image']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'image', 'descricao', 'dataInicio', 'dataFim', 'hora_inicio', 'hora_final', 'dias', 'valor_cur', 'fk_idCaCursos', 'fk_idFuncionario' ]


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['fk_idCaCursos','fk_idCurso', 'fk_idMetodoPagamento',]