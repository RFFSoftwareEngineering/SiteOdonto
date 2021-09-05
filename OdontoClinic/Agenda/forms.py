from django import forms
from .models import Agendamento


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = [
            "PrimeiroNome",
            "Sobrenome",
            "Telefone",
            "Dor",
            "Problema"
        ]
