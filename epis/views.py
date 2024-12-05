from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from db_mvhs.models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required# Create your views here.
def epis(request):
    return render(request,'epis.html')



class formulario_epis(CreateView):
    model = epis_base
    fields = '__all__'
    template_name = 'formularios.html'

    def get_success_url(self):
        return reverse_lazy('Inicio:index')
    
class formulario_uniformes(CreateView):
    model = uniformes_base
    fields = '__all__'
    template_name = 'formularios.html'

    def get_success_url(self):
        return reverse_lazy('Inicio:index')
    
class formulario_outros(CreateView):
    model = outros_base
    fields = '__all__'
    template_name = 'formularios.html'

    def get_success_url(self):
        return reverse_lazy('Inicio:index')