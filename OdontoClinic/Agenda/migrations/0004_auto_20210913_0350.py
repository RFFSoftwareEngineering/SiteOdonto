# Generated by Django 3.2.6 on 2021-09-13 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0003_auto_20210913_0339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='data',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='horario',
        ),
    ]