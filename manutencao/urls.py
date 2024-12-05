from django.urls import path

from manutencao import views as v

app_name = 'manutencao'


urlpatterns = [
    path('', v.manutencao, name='manu'),

    
    path('manutencao_lista/',
          v.manutencao_lista.as_view(),
            name='manutencao_lista'),
  
    path('acao_manutencao/',
          v.acao_manutencao.as_view(),
            name='acao_manutencao'),

    path('agendamento_lista/',
          v.agendamento_lista.as_view(),
            name='agendamento_lista'),
     
    
]