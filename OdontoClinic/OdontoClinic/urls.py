"""OdontoClinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import HomePage, ServicesPage
from Agenda.views import (teste_view,
                          manipulate_view,
                          calendar_view,
                          marcar_view)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePage, name="home"),
    path("services/", ServicesPage, name="servicos"),
    path("Agendamento/<int:id>/", teste_view , name="teste"),
    path("teste", manipulate_view),
    path("Calendar/", calendar_view, name="calendar"),
    path("Calendar/<int:lista_dias_clean>/", marcar_view, name="marcar")
    ]
