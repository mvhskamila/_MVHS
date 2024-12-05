from django.urls import path

from frota import views as v

app_name = 'frota'


urlpatterns = [
    path('', v.frota, name='frota'),

    path('formulario_td/',
          v.formuloario_td.as_view(),
            name='formulario_td'),  

    path('td_list/',
          v.td_list.as_view(),
            name='td_list'),    

    path('formulario_revenda/',
          v.formulario_revenda.as_view(),
            name='formulario_revenda'),

    path('revenda_lista/',
          v.revenda_lista.as_view(),
            name='revenda_lista'),

    path('revenda_OK/',
          v.revenda_ok,
            name='revenda_OK'),
    
    path('formulario_manutencao/',
          v.formulario_manutencao.as_view(),
            name='formulario_manutencao'),

    path('ver_lista_carga/',
          v.ver_lista_carga.as_view(),
            name='ver_lista_carga'),

]