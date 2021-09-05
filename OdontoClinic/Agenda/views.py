from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Agendamento
from .forms import AgendaForm
from datetime import datetime

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
