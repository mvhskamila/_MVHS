from django.shortcuts import render
from administrativo import views
from django.views.generic import CreateView,ListView,DateDetailView
from db_mvhs.models import *
from db_mvhs.forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def frota(request):
    return render(request, 'frota.html')

class formuloario_td(CreateView):
    model = tab_td      
    template_name = 'formularios.html'
    form_class = forms_td

class td_list(ListView):
    model = tab_td
    template_name = 'td_list.html'
    paginate_by = 15


class formulario_revenda(CreateView):
    model = Revenda      
    template_name = 'formularios.html'
    form_class = forms_revenda

class revenda_lista(ListView):
    model = Revenda
    template_name = 'lista_revenda.html'
    paginate_by = 5


def revenda_ok(request):
    return render(request, 'revenda_ok.html')

class formulario_manutencao(CreateView):
    model = Manutencao      
    template_name = 'formularios.html'
    form_class = forms_manutencao

class ver_lista_carga(ListView):
    model =Cargas    
    template_name= 'ver_lista_cargas.html'       
    paginate_by=5
    