from django.urls import path

from Inicio import views as v

app_name = 'Inicio'


urlpatterns = [
    path('', v.index, name='index'),
]