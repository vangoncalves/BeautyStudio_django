# Generated by Django 5.1 on 2024-09-03 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BStudios', '0002_remove_servico_fk_idcaservicos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='data_hora',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='hora',
        ),
        migrations.AddField(
            model_name='agendamento',
            name='fk_idCaCursos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BStudios.cacursos'),
        ),
    ]
