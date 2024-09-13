from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Usuario

class UserAdmin(BaseUserAdmin):
    # Formulário de exibição de usuários no Django Admin
    list_display = ('username', 'email', 'nome', 'telefone', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'telefone')}),
        ('Permissões', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nome', 'telefone', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ()

# Registrar o modelo de usuário personalizado no admin
admin.site.register(Usuario, UserAdmin)

# Remover o grupo (opcional, se você não for usá-lo)
admin.site.unregister(Group)