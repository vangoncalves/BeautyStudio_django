from django import forms
from .models import CaCursos, Curso, Pedido

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

'''class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fk_idCurso', 'fk_idCaCursos']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Exibir apenas cursos disponíveis para o usuário
            self.fields['curso'].queryset = Curso.objects.all()'''