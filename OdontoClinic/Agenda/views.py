from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Agendamento
from .forms import AgendaForm
from datetime import datetime
import calendar

ano = datetime.now().strftime("%Y")
ano_clean = int(ano)
mes = datetime.now().strftime("%m")
mes_clean = int(mes)
dia = datetime.now().strftime("%d")
dia_clean = int(dia)

if mes_clean == 1:
    mes_clean_name = "Janeiro"
elif mes_clean == 2:
    mes_clean_name = "Fevereiro"
elif mes_clean == 3:
    mes_clean_name = "Março"
elif mes_clean == 4:
    mes_clean_name = "Abril"
elif mes_clean == 5:
    mes_clean_name = "Maio"
elif mes_clean == 6:
    mes_clean_name = "Junho"
elif mes_clean == 7:
    mes_clean_name = "Julho"
elif mes_clean == 8:
    mes_clean_name = "Agosto"
elif mes_clean == 9:
    mes_clean_name = "Setembro"
elif mes_clean == 10:
    mes_clean_name = "Outubro"
elif mes_clean == 11:
    mes_clean_name = "Novembro"
elif mes_clean == 12:
    mes_clean_name = "Dezembro"

lista_dias = []
obj_calendar = calendar.Calendar()

for day in obj_calendar.itermonthdays(ano_clean, mes_clean):
    lista_dias.append(day)

lista_dias_clean = list(set(lista_dias))

now = datetime.now().strftime('%H:%M:%S')

def teste_view(request, id, *args, **kwargs):
    obj = get_object_or_404(Agendamento, id=id)
    obj = Agendamento.objects.get(id=id)
    context = {
        "object" : obj,
        "actual_time": now
        }
    return render(request, "Agendamento/teste.html", context)

def manipulate_view(request, *args, **kwargs):
    form = AgendaForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form" : form,
        "actual_time" : now
        }
    return render(request, "Agendamento/form_test.html", context)

def calendar_view(request, *args, **kwargs):
    form = AgendaForm(request.POST or None)
    if form.is_valid():
        form.save()      
    context = {
        "dados" : form,
        "actual_time" : now,
        "ano" : ano_clean,
        "mes" : mes_clean_name,
        "a_lista" : lista_dias,
        "hoje" : dia_clean,
        "links" : lista_dias_clean
        }
    return render(request, "Agendamento/calendar.html", context)

def marcar_view(request, lista_dias_clean, *args, **kwargs):
    context = {
        "links" : lista_dias_clean,
        "actual_time" : now
        }
    return render(request, "Agendamento/marcar.html", context)
