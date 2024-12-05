import csv
from django.shortcuts import render
from db_mvhs.models import *
from db_mvhs.forms import *
from django.views.generic import  CreateView,ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def abastecimento(request):
    return render(request,'abastecimento.html')

class formulario_Abastecimento(CreateView):
    model = Abastecimento
    form_class = forms_Abastecimento
    template_name = 'formularios.html'

class Abastecimento_lista(ListView):
    model = Abastecimento
    template_name = 'abastecimento_lista.html'
    paginate_by = 10

def abastecimento_imprimir(request):
    object_list=Abastecimento.objects.all()
    d1=request.GET.get('d1')
    d2=request.GET.get('d2')
    media=0
    valor=0
    contador=0
    acao='Imprimir pesquisa entre datas'
    texto= d1, d2
    if d1 and d2:
        object_list=object_list.filter(data__range=[d1,d2])


    context = {
        'acao':acao,
        'texto':texto
    }
    if d1 and d2:
        if context:
            # Create the HttpResponse object with the appropriate CSV header.
            response = HttpResponse(
                content_type="text/csv",
                headers={"Content-Disposition": 'attachment; filename="MVHS_abastecimento.csv"'},
            )

            writer = csv.writer(response)
            context = ('MVHS INFORMAÇÕES',' ','Relatorio de abastecimento')
            writer.writerow(context)
            context = (' ')
            writer.writerow(context)
            writer.writerow(['MOTORISTA','KM','HORIMETRO','LITROS','HODOMETRO','DATA','HORA',
                            'PLACA','RESPONSAVEL'])

            #object_list=Revenda.objects.all()
            for object_list in object_list:
                texto=(object_list.Nome_motorista,
                       object_list.km,
                       object_list.horimetro,
                       object_list.Litros,
                       object_list.hodometro,
                       #formatar data não esquecer
                       object_list.data,
                       object_list.hora,
                       object_list.Abastecimento_placa,
                       object_list.responsave_abastecimento
                       )
                valor=(valor +object_list.Litros)
                    #contador=contador+1
                if d1 == d2:
                        contador=1
                        media =valor/contador
                else:
                        contador=contador+1
                        media =valor/contador

                writer.writerow(texto)

            #media =valor/contador
            totalizacao=('Totalização','dos', 'dados', 'registrados')
            writer.writerow(' ')
            writer.writerow(totalizacao)
            writer.writerow(' ')
            context = ('Numero de abastecimentos','media','Litros')
            writer.writerow(context)
            context = (contador,media,valor)
            writer.writerow(context)
            writer.writerow(' ')
            writer.writerow(' ')
            context = ('MVHS','.','INFORMAÇÕES')
            writer.writerow(context)

            return response
    return render(request, 'pes_imprimir.html',context)  
    
    
