from django.urls import path

from abastecimento import views as v

app_name = 'abastecimento'


urlpatterns = [
    path('', v.abastecimento, name='abastecimento'),

    path('formulario_Abastecimento/',
          v.formulario_Abastecimento.as_view(),
            name='formulario_Abastecimento'),

    path('Abastecimento_lista/',
          v.Abastecimento_lista.as_view(),
            name='Abastecimento_lista'),

    path('abastecimento_imprimir/',
          v.abastecimento_imprimir,
            name='abastecimento_imprimir'),

]