# Generated by Django 3.2.6 on 2021-09-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='horario',
            field=models.TimeField(),
        ),
    ]