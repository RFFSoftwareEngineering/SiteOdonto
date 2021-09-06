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
    x = 1
    obj = get_object_or_404(Agendamento, id=x)
    obj = Agendamento.objects.get(id=x)
    context = {
        "dados" : form,
        "actual_time" : now,
        "object" : obj
        }
    return render(request, "Agendamento/calendar.html", context)
