import statistics
import csv
from django.http import HttpResponse
from django.shortcuts import render,redirect
from db_mvhs.models import *
from db_mvhs.forms import *
from django.views.generic import  ListView,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def force_logout(request):
    logout(request)
    context='<h1>Voce saiu do sistema! |---MVHS Informações---|</h1><p><a href="/"type="button" class="button_adm"><h1>Inicio</h1></a></p>'
    return HttpResponse(context)

def nao_autorizado(request):
    logout(request)
    context='<h1>Não foi autorizado! |---MVHS Informações---|</h1><p><a href="/"type="button" class="button_adm"><h1>Inicio</h1></a></p>'
    return HttpResponse(context)

@login_required
def adm(request):
    if request.user.is_superuser:
        return render(request, 'adm.html')
    else:
        return nao_autorizado(request)
    #return render(request, 'adm.html')



class formulario_caminhao(CreateView):
        model =Caminhao
        template_name= 'formularios.html'
        form_class=forms_caminhao
        def is_valid(self):
            valid = super(formulario_caminhao, self).is_valid()
            if not valid:
                return False
            return True
        
        def form_valid(self, form):
            form.save()
            return super(formulario_caminhao, self).form_valid(form)
        
        def form_invalid(self, form):
            return super().form_invalid(form)
    
class formulario_Motorista(CreateView):
    model =Motorista
    template_name= 'formularios.html'
    form_class=forms_Motorista

class formulario_Ajudante(CreateView):
    model =Ajudante
    template_name= 'formularios.html'
    form_class=forms_Ajudante

class formulario_cargas(CreateView):
    model =Cargas
    template_name= 'formularios.html'
    form_class=forms_Cargas

    def get_context_data(self,*args, **kwargs):
        context = super(formulario_cargas,self).get_context_data(*args,**kwargs)
        request=self.request
        if request.user.is_superuser:
            return context
        else:
            reverse_lazy('administrativo:nao_autorizado')
    
    def is_valid(self):
        valid = super(formulario_cargas, self).is_valid()
        if not valid:
            return False
        return True
    def form_valid(self, form):
        form.save()
        return super(formulario_cargas, self).form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)       
    

        
class fornulario_lista(ListView):
    model =Cargas    
    template_name= 'lista_cargas.html'       
    paginate_by=5

class caminhao_lista(ListView):
     model =Caminhao    
     template_name= 'lista_caminhao.html'
     paginate_by=10

class motorista_lista(ListView):
     model =Motorista    
     template_name= 'lista_motorista.html'
     paginate_by=10

class ajudante_lista(ListView):
     model =Ajudante    
     template_name= 'lista_ajudante.html'
     paginate_by=10

    
def pesquisar_revenda(request):
    object_list=Revenda.objects.all()
    d1=request.GET.get('d1')
    d2=request.GET.get('d2')
    acao='Pesquisar entre datas'

    texto= d1, d2
    if d1 and d2:
        object_list=object_list.filter(entrada__range=[d1,d2])

   
    
    context = {
        'acao':acao,
        'texto':texto,
        'object_list':object_list

    }
    return render(request, 'revenda_pesquisar.html',context)

#soma com tara de cada caminhão por placa
def soma(object_list,tara):
    sp2=0
    sp5=0
    sp8=0
    sp13=0
    sp20=0
    sp45=0
    skm=0
    km_retorno=0
    km_saida=0

    obj=object_list.all()
    contador=object_list.count()

    for obj in obj:
        skm=skm+obj.km
        acao=obj.acao
        sp2=sp2+obj.p2
        sp5=sp5+obj.p5
        sp8=sp8+obj.p8
        sp13=sp13+obj.p13
        sp20=sp20+obj.p20
        sp45=sp45+obj.p45
        sobj=(((sp2*5)+(sp5*12)+(sp8*16)+(sp13*28)+(sp20*60)+(sp45*90)))
        if acao == 'SAIDA' or acao == 'RETORNO':
            contador=contador-1
        if acao == 'SAIDA':
            km_saida=obj.km
        if acao == 'RETORNO':
            km_retorno=obj.km

    cont=sobj/contador
    csp2=sp2/contador
    csp5=sp5/contador
    csp8=sp8/contador
    csp13=sp13/contador
    csp20=sp20/contador
    csp45=sp45/contador

    cskm= skm
    mediacskm= km_retorno - km_saida
    soma_tara= tara*contador
    mediana=[sp2,sp5,sp8,sp13,sp20,sp45]
    calc_mediana=statistics.median(mediana)
    calc_mediana_baixa=statistics.median_low(mediana)
    calc_mediana_alta=statistics.median_high(mediana)
    calc_media_aritimetica=statistics.mean(mediana)
    calc_media_Harmonica = statistics.harmonic_mean(mediana)


    context = {
        'sp2'  :sp2,'sp5':sp5,'sp8':sp8,'sp13':sp13,
        'sp20' :sp20,'sp45':sp45,'sobj' :sobj,'cont':cont,
        'csp2' :csp2,'csp5':csp5,'csp8':csp8,
        'csp13':csp13,'csp20':csp20,'csp45':csp45,
        'mediacskm':mediacskm,'contador':contador,'soma_tara':soma_tara,
        'calc_mediana':calc_mediana,'calc_mediana_baixa':calc_mediana_baixa,
        'calc_mediana_alta':calc_mediana_alta,'cskm':cskm,
        'calc_media_aritimetica':calc_media_aritimetica,
        'calc_media_Harmonica':calc_media_Harmonica,

    }

    return context
#soma para a pesquisa td e data
def soma_restrita_sem_tara(object_list):

    sp2=0
    sp5=0
    sp8=0
    sp13=0
    sp20=0
    sp45=0
    skm=0
    cskm=0

    obj=object_list.all()
    contador=object_list.count()

    for obj in obj:
        skm=skm+obj.km
        sp2=sp2+obj.p2
        sp5=sp5+obj.p5
        sp8=sp8+obj.p8
        sp13=sp13+obj.p13
        sp20=sp20+obj.p20
        sp45=sp45+obj.p45
        acao=obj.acao
        sobj=(((sp2*5)+(sp5*12)+(sp8*16)+(sp13*28)+(sp20*60)+(sp45*90)))
        if acao == 'SAIDA' or acao == 'RETORNO':
            contador=contador-1
        if acao == 'SAIDA':
            km_saida=obj.km
        if acao == 'RETORNO':
            km_retorno=obj.km

    mediacskm= km_retorno - km_saida

    cont=sobj/contador
    csp2=sp2/contador
    csp5=sp5/contador
    csp8=sp8/contador
    csp13=sp13/contador
    csp20=sp20/contador
    csp45=sp45/contador

    t_obj= Caminhao.objects.all()

    for t_obj in t_obj:
        cskm= cskm + t_obj.tara


    mediana=[sp2,sp5,sp8,sp13,sp20,sp45]
    calc_mediana=statistics.median(mediana)
    calc_mediana_baixa=statistics.median_low(mediana)
    calc_mediana_alta=statistics.median_high(mediana)
    calc_media_aritimetica=statistics.mean(mediana)
    calc_media_Harmonica = statistics.harmonic_mean(mediana)


    context = {
        'sp2':sp2,'sp5':sp5,'sp8':sp8,'sp13':sp13,
        'sp20':sp20,'sp45':sp45,'sobj' :sobj ,
        'cont':cont,'csp2':csp2,
        'csp5':csp5,'csp8':csp8,'csp13':csp13,
        'csp20':csp20,'csp45':csp45,'cskm':cskm,
        'mediacskm':mediacskm,'contador':contador,
        'calc_mediana':calc_mediana,'calc_mediana_baixa':calc_mediana_baixa,
        'calc_mediana_alta':calc_mediana_alta,'soma_tara':cskm,
        'calc_media_aritimetica':calc_media_aritimetica,
        'calc_media_Harmonica':calc_media_Harmonica,

    }

    return context

#pesquisar
def pesquisar_td(request):
    q=''
    #pesquisa por td
    if 'qtd'in request.GET:
        q=request.GET['qtd']
        if q != '':
            tab_tds=tab_td.objects.all()
            A=tab_tds.filter(td__exact=q)
            if A :
                A=tab_tds.get(td__exact=q)
            else:
                return render(request, 'pesquisar_td.html')
                #pega o id da linha consultada
            B=A.id

            object_list = Revenda.objects.filter(link_td__exact=B)
            soma_context=soma_restrita_sem_tara(object_list)
            context = {
                    'soma_context':soma_context,
                    'object_list' :object_list
                    }
            return render(request, 'pesquisar_td.html',context)
        else:
            return render(request, 'pesquisar_td.html')

    else:
        #pesquisa por placa
        if 'qp'in request.GET:
            qp=request.GET['qp']
            if qp!='':
                tab_caminhao=Caminhao.objects.all()
                A=tab_caminhao.filter(placa_veiculo__icontains=qp)
                if A :
                    A=tab_caminhao.get(placa_veiculo__icontains=qp)
                else:
                    return render(request, 'pesquisar_td.html')
                #pega o id da linha consultada
                B=A.id
                tara=A.tara
                #pesquisa a tabela Revenda atravez do valor id (B)
                object_list = Revenda.objects.filter(link_caminhao__exact=int(B))


                soma_context=soma(object_list,tara)
                context = {
                    'soma_context':soma_context,
                    'object_list' :object_list}
                return render(request, 'pesquisar_td.html',context)
            else:
                return render(request, 'pesquisar_td.html')
        else:
            if 'qd'in request.GET:
                qd=request.GET['qd']
                if qd!='':
                    object_list=Revenda.objects.filter(entrada__contains=qd)
                    if object_list:
                        soma_context=soma_restrita_sem_tara(object_list)
                    else:
                        return render(request, 'pesquisar_td.html')

                    context = {
                    'soma_context':soma_context,
                    'object_list' :object_list}
                    return render(request, 'pesquisar_td.html',context)
                else:
                    return render(request, 'pesquisar_td.html')

    lista_placa=Caminhao.objects.all()
    
    context_placa={
        'lista_placa':lista_placa
    }

    return render(request, 'pesquisar_td.html',context_placa)


def pes_imprimir(request):
    object_list=Revenda.objects.all()
    d1=request.GET.get('d1')
    d2=request.GET.get('d2')
    retorno=''
    media=''
    acao='Imprimir pesquisa entre datas'

    texto= d1, d2
    if d1 and d2:
        object_list=object_list.filter(entrada__range=[d1,d2])
        retorno=object_list

    context = {
        'acao':acao,
        'texto':texto

    }

    if d1 and d2:
        if context:

            # Create the HttpResponse object with the appropriate CSV header.
            response = HttpResponse(
                content_type="text/csv",
                headers={"Content-Disposition": 'attachment; filename="MVHS_informações.csv"'},
            )

            writer = csv.writer(response)
            writer.writerow(['TD','Veiculo','Motorista','Ajudante','Km','Cliente',
                            'Codigo do cliente','Nf 1','Nf 2','p2','p5','p8','p13','p20',
                            'p45','Data',"Horario",'OBS'])

            #object_list=Revenda.objects.all()
            for object_list in object_list:
                texto=(object_list.link_td,object_list.link_caminhao,object_list.link_motorista,object_list.link_Ajudante,object_list.km,object_list.cliente,
                            object_list.codigo_cliente,object_list.nota_1,object_list.nota_2,object_list.p2,object_list.p5,object_list.p8,object_list.p13,object_list.p20,
                            object_list.p45,object_list.entrada,object_list.horario,object_list.OBS)
                writer.writerow(texto)


            sp2=0
            sp5=0
            sp8=0
            sp13=0
            sp20=0
            sp45=0
            sobject_list=0
            valor=0
            #preco=0
            contador=0
            total=0
            object_list=retorno


            for object_list in object_list:

                #ssoma=float(object_list.soma)
                sp2=(sp2+object_list.p2)
                sp5=(sp5+object_list.p5)
                sp8=(sp8+object_list.p8)
                sp13=(sp13+object_list.p13)
                sp20=(sp20+object_list.p20)
                sp45=(sp45+object_list.p45)
                sobject_list=(sp2*8)+(sp5*12)+(sp8*16)+(sp13*28)+(sp20*60)+(sp45*90)
                valor=(sobject_list)
                    #preco=(ssoma)
                contador=contador+1
                media=float(sobject_list/contador)
                total=(valor)
            #total=valor*preco
            #total=total/28
            totalizacao=('Totalização','dos', 'dados', 'registrados')
            writer.writerow(' ')
            writer.writerow(totalizacao)
            writer.writerow(' ')
            context = ('sp2','sp5','sp8','sp13','sp20','sp45','Numero de entregas','media','total')
            writer.writerow(context)
            context = (sp2,sp5,sp8,sp13,sp20,sp45,contador,media,total)
            writer.writerow(context)

            return response
    return render(request, 'pes_imprimir.html',context)

def reiniciar_tabela_carga(request):
        return  render(request,'info.html')

def del_itens_tab_carga(request):
        objects=Cargas.objects.all()
        objects.delete()
        texto="Tabela foi reiniciada com sucesso!"
        context={'texto':texto}
        return  render(request,'info.html',context)


