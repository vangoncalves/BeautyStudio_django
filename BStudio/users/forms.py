# BStudio/BStudios/users/forms.py
from django import forms
from .models import Usuario

class UsuarioRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}), label="Senha")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Senha'}), label="Confirmar Senha")

    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'email', 'username']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'As senhas não coincidem.')


class SuperUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}), label="Senha")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Senha'}), label="Confirmar Senha")

    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'email', 'username']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
            }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'As senhas não coincidem.')