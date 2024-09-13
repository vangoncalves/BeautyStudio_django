from django import forms
from .models import CaCursos, Curso, Pedido, MetodoPagamento

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

class MetodoPagamentoForm(forms.Form):
    metodo_pagamento = forms.ModelChoiceField(
        queryset=MetodoPagamento.objects.all(),
        empty_label="Escolha um método de pagamento",
        widget=forms.Select
    )

