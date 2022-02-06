from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (ListView , UpdateView , DeleteView , CreateView)
from .models import Funcionario

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin


class FuncionariosList(ListView , LoginRequiredMixin):
    model = Funcionario

    def get_queryset(self , ):
        empresa_logada = self.request.user.funcionario.empresa

        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UserPassesTestMixin, UpdateView, ):
    model = Funcionario

    fields = ['nome' , 'departamentos']



    def test_func(self, ):
        funcionario = self.get_object()
        return funcionario.empresa == self.request.user.funcionario.empresa


    def get_permission_denied_message(self):
        return 'Permisão negada'




class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario

    fields = ['nome' , 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)

        return super(FuncionarioCreate, self).form_valid(form)
