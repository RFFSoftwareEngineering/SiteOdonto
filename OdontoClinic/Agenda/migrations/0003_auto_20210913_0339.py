# Generated by Django 3.2.6 on 2021-09-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0002_auto_20210913_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='horario',
            field=models.TimeField(blank=True),
        ),
    ]
