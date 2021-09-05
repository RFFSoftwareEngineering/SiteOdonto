from django.db import models
from django.urls import reverse


class Agendamento(models.Model):
    id           = models.AutoField(auto_created=True, primary_key=True)
    PrimeiroNome = models.CharField(max_length=50, blank=False)
    Sobrenome    = models.CharField(max_length=50, blank=False)
    Telefone     = models.CharField(max_length=50, default="(00)00000-0000", blank=False)
    Dor          = models.BooleanField(default=False, blank=False)
    Problema     = models.TextField(default="descreva o que sente", blank=False)



