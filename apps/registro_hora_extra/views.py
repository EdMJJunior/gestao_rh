import json
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView , UpdateView , DeleteView , CreateView
from .forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra
from apps.funcionarios.models import Funcionario
# Create your views here.


class HoraExtraList(ListView):
    model = RegistroHoraExtra


    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)




class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs


class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    # success_url = reverse_lazy('edit_hora_extra')

    def get_success_url(self):
        return reverse_lazy('edit_hora_extra', args=[self.object.id])


    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs



class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs




class UtilizouHoraExtra(View):
    def post(request,*args, **kwargs):
        l_funcionarios = list(Funcionario.objects.all())
        data = {}
        with open('/home/junior/gestao_rh/staticfiles/json/output.json') as json_file:
            data = json.load(json_file)

        hora = RegistroHoraExtra()
        while l_funcionarios:
            funcionario = l_funcionarios.pop()
            campos = data.pop()

            hora.motivo = campos['motivo']
            hora.horas = campos['horas']
            hora.funcionario = funcionario
            hora.save()



        response = json.dumps({'mensagem' : 'requisição execultada'})
        
        return HttpResponse(response, content_type='application/json')