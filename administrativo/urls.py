from django.urls import path

from administrativo import views as v

from django.contrib.auth import views as auth_views
app_name = 'administrativo'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', v.force_logout, name='logout'),
    path('nao_autorizado/', v.nao_autorizado, name='nao_autorizado'),
    path('', v.adm, name='admin'),
    
    path('formulario_motorista/',
          v.formulario_Motorista.as_view(),
            name='formulario_motorista'),

    path('formulario_ajudante/',
          v.formulario_Ajudante.as_view(),
            name='formulario_ajudante'),

    path('formulario_caminhao/',
          v.formulario_caminhao.as_view(),
            name='formulario_caminhao'),

    path('formulario_cargas/',
          v.formulario_cargas.as_view(),
            name='formulario_cargas'),

    path('fornulario_lista/',
          v.fornulario_lista.as_view(),
            name='fornulario_lista'),

    path('caminhao_lista/',
          v.caminhao_lista.as_view(),
            name='caminhao_lista'),

    path('motorista_lista/',
          v.motorista_lista.as_view(),
            name='motorista_lista'),

    path('ajudante_lista/',
          v.ajudante_lista.as_view(),
            name='ajudante_lista'),

    path('pesquisar_revenda/',
          v.pesquisar_revenda,
            name='pesquisar_revenda'),

    path('pesquisar_td/',
          v.pesquisar_td,
            name='pesquisar_td'),
            
    path('pes_imprimir/',
          v.pes_imprimir,
            name='pes_imprimir'),

    path('reiniciar_tabela_carga',
          v.reiniciar_tabela_carga,
            name='reiniciar_tabela_carga'),

    path('del_itens_tab_carga',
          v.del_itens_tab_carga,
            name='del_itens_tab_carga'),
   
 
]