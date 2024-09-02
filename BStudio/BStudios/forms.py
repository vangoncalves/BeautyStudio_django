from django import forms
from .models import Agendamento

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data_hora', 'hora', 'fk_idMetodoPagamento',]