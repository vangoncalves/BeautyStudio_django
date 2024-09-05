from django import forms
from .models import Usuario 
from .models import Agendamento, CaCursos, Curso

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

class Usuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'email', 'username']
        labels = {'nome':'', 'telefone':'', 'email':'', 'username':''}