# Generated by Django 5.0.7 on 2024-09-17 16:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaCursos',
            fields=[
                ('idCaCursos', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='image/categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('idFuncionario', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('telefone', models.CharField(max_length=11)),
                ('cargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPagamento',
            fields=[
                ('idMetodoPagamento', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idCurso', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='image/curso')),
                ('descricao', models.CharField(max_length=300)),
                ('dataInicio', models.DateField()),
                ('dataFim', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('dias', models.CharField(max_length=100)),
                ('valor_cur', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fk_idCaCursos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BStudios.cacursos')),
                ('fk_idFuncionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BStudios.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idPedido', models.BigAutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('fk_idCaCursos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BStudios.cacursos')),
                ('fk_idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BStudios.curso')),
                ('fk_idMetodoPagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BStudios.metodopagamento')),
                ('fk_idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
