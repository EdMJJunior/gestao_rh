from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.urls import reverse

from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa

    fields = ['nome']
    success_url = 'home'


    def form_valid(self, form):
        obj = form.save()

        funcionario = self.request.user.funcionario

        funcionario.empresa = obj
        funcionario.save()

        return redirect(self.success_url)



class EmpresaEdit(UpdateView):
    model = Empresa

    fields = ['nome']



