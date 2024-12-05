from django.urls import path

from epis import views as v

app_name = 'epis'


urlpatterns = [
    path('', v.epis, name='epis'),

    path('formulario_epis/',
          v.formulario_epis.as_view(),
            name='formulario_epis'),

    path('fomulario_uniformes',
          v.formulario_uniformes.as_view(),    
            name='formulario_uniformes'),

    path('formulario_outros',
          v.formulario_outros.as_view(),    
            name='formulario_outros'),    

    
]