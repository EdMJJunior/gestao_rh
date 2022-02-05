from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView
)
from .models import Departamento


class Departamentolist(ListView):
    model = Departamento

    def get_queryset(self,):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)



class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        return super(DepartamentoCreate, self).form_valid(form)



class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamentos')




class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')