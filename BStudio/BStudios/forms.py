from django import forms
from .models import CaCursos, Curso, MetodoPagamento

class CaCursosForm(forms.ModelForm):
    class Meta:
        model = CaCursos
        fields = ['nome', 'image']
        labels = {'nome': ''}

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'image', 'descricao', 'dataInicio', 'dataFim', 'hora_inicio', 'hora_final', 'dias', 'valor_cur', 'fk_idCaCursos', 'fk_idFuncionario' ]
        widgets = {'descricao':forms.Textarea(attrs={'cols':9})}

class MetodoPagamentoForm(forms.ModelForm):
    class Meta:
        model = MetodoPagamento
        fields = ['tipo' ]
