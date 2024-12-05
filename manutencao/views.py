from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from db_mvhs.models import *
from manutencao.models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def manutencao(request):
    return render(request, 'manu.html')


class manutencao_lista(ListView):
    model = Manutencao       
    template_name = 'manutencao_lista.html'     

    def get_queryset(self):
        return Manutencao.objects.all().order_by('-data')   
    
class acao_manutencao(CreateView):
    model = Manutencao_Resposta
    fields = '__all__'
    template_name = 'formularios.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)   
    
class agendamento_lista(ListView):
    model = Manutencao_Resposta
    template_name = 'agendamento_lista.html'

    def get_queryset(self):
        return Manutencao_Resposta.objects.all().order_by('-data')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agendamento'] = Manutencao_Resposta.objects.all().order_by('-data')
        return context
    

    
