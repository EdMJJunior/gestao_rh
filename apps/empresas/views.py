from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic.edit import CreateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa

    fields = ['nome']

    success_url = '/'


    def form_valid(self, form):
        obj = form.save()

        funcionario = self.request.user.funcionario

        funcionario.empresa = obj
        funcionario.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return '/'






