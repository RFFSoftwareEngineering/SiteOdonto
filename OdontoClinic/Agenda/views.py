from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Agendamento
from .forms import AgendaForm

def teste_view(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    obj = Agendamento.objects.get(id=id)
    context = {
        "object" : obj
        }
    return render(request, "Agendamento/teste.html", context)

def manipulate_view(request):
    form = AgendaForm(request.POST or None)
    if form is_valid():
        form.save()
    context = {
        "form" : form
        }
    return render(request, "Agendamento/form_test.html", context)
