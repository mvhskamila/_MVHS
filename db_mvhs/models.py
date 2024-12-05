from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from db_mvhs.restrito import *
# Create your models here.
# Create your models here.
class Motorista(models.Model):
    data = models.DateTimeField('criado em',auto_now_add=True,auto_now=False )
    motorista = models.CharField(max_length=30, blank=True, null=True,unique=True)
    
    def __str__(self):
        return self.motorista
    class Meta:
        ordering = ('-data',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(Motorista)
        permission = Permission.objects.filter(content_type=content_type, codename='administrativo')
        return permission
    
    def get_absolute_url(self):
        return reverse_lazy('Inicio:index')

class Ajudante(models.Model):
    data = models.DateTimeField('criado em',auto_now_add=True,auto_now=False )
    ajudante = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.ajudante
    class Meta:
        ordering = ('-data',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(Ajudante)
        permission = Permission.objects.filter(content_type=content_type, codename='administrativo')
        return permission
    
    def get_absolute_url(self):
        return reverse_lazy('Inicio:index')

class Caminhao(models.Model):
    placa_veiculo = models.CharField(max_length=8, blank=False, null=False,unique=True)
    km = models.IntegerField(default=0,blank=True, null=True)
    tara = models.IntegerField(default=0,blank=True, null=True)

    def __str__(self):
        return self.placa_veiculo
    class Meta:
        ordering = ('placa_veiculo',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(Caminhao)
        permission = Permission.objects.filter(content_type=content_type, codename='administrativo')
        return permission
    def get_absolute_url(self):
        return reverse_lazy('administrativo:caminhao_lista')


class tab_td(models.Model):
    td = models.IntegerField(default=0,blank=True, null=True,unique=True)
    saida_base = models.DateTimeField('criado em',
        auto_now_add=True,
        auto_now=False )
    link_reponsavel = models.ForeignKey(Motorista, on_delete=models.CASCADE, null=True, blank=True,related_name="link_reponsavel")
    link_placa = models.ForeignKey(Caminhao, on_delete=models.CASCADE, null=True, blank=True,related_name="link_reponsavel")
   
    class Meta:
        ordering = ('-saida_base',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(tab_td)
        permission = Permission.objects.filter(content_type=content_type, codename=['administrativo','frota' ]   )
        return permission
    def get_absolute_url(self):
        return reverse_lazy('Inicio:index')

    def __str__(self):
        return '{}-{}-{}'.format(self.td,self.link_reponsavel,self.link_placa)

acao=(
('SAIDA','saida'),
('REVENDA','revenda'),
('RETORNO','retorno')
)
class Revenda(models.Model):
    acao = models.CharField(max_length=7, choices=acao, blank=True)
    km = models.IntegerField(default=0,blank=True, null=True)
    cliente = models.CharField(max_length=30, blank=True, null=True)
    codigo_cliente = models.IntegerField(default=0,blank=True, null=True)
    nota_1 = models.IntegerField(default=0,blank=True, null=True)
    nota_2 = models.IntegerField(default=0,blank=True, null=True)
    p2 = models.IntegerField(default=0,blank=True, null=True)
    p5 = models.IntegerField(default=0,blank=True, null=True)
    p8 = models.IntegerField(default=0,blank=True, null=True)
    p13 = models.IntegerField(default=0,blank=True, null=True)
    p20 = models.IntegerField(default=0,blank=True, null=True)
    p45 = models.IntegerField(default=0,blank=True, null=True)
    entrada = models.DateField('criado em',
        auto_now_add=True,
        auto_now=False )
    horario = models.TimeField('criado em',
        auto_now_add=True,
        auto_now=False)
    OBS = models.CharField(max_length=254, blank=True, null=True)
    link_caminhao = models.ForeignKey(Caminhao,on_delete=models.CASCADE, null=True, blank=True,related_name="link_caminhaos")  # One-to-many relationshi
    link_motorista = models.ForeignKey(Motorista,on_delete=models.CASCADE, null=True, blank=True,related_name="link_motoristas")  # One-to-many relationshi
    link_Ajudante = models.ForeignKey(Ajudante,on_delete=models.CASCADE, null=True, blank=True,related_name="link_ajudantes")  # One-to-many relationshi
    link_td = models.ForeignKey(tab_td,on_delete=models.CASCADE, null=True, blank=True,related_name="link_tds")  # One-to-many relationshi

    class Meta:
        ordering = ('-entrada',)
    def __int__(self):
        return self.cliente
    
    def permission(self):
        content_type = ContentType.objects.get_for_model(Revenda)
        permission = Permission.objects.filter(content_type=content_type, codename=['administrativo','frota'])
        return permission
    def get_absolute_url(self):
        return reverse_lazy('frota:revenda_OK')



class Manutencao(models.Model):

    responsavel = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField('criado em',auto_now_add=True,auto_now=False )
    horario = models.TimeField('criado em',auto_now_add=True,auto_now=False )
    link_descricao = models.ForeignKey(Caminhao, on_delete=models.CASCADE, null=True, blank=True,related_name="link_descricao")  # One-to-one relationship
    # não pode ser CAsCADE de apagar somente o registro
    def __str__(self):
        return self.responsavel
    class Meta:
        ordering = ('-data',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(Manutencao)
        permission = Permission.objects.filter(content_type=content_type, codename=['administrativo','manutencao'])
        return permission
    def get_absolute_url(self):
        return reverse_lazy('Inicio:index')

class Manutencao_Resposta(models.Model):

    responsavel = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    Agendado = models.DateField('Data: Agendada')
    data = models.DateField('criado em',auto_now_add=True,auto_now=False )
    horario = models.TimeField('criado em',auto_now_add=True,auto_now=False )
    link_agendado = models.ForeignKey(Caminhao, on_delete=models.CASCADE, null=True, blank=True,related_name="link_agendado")  # One-to-one relationship
    # não pode ser CAsCADE de apagar somente o registro
    def __str__(self):
        return self.responsavel
    class Meta:
        ordering = ('-data',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(Manutencao)
        permission = Permission.objects.filter(content_type=content_type, codename=['administrativo','manutencao','frota'])
        return permission
    def get_absolute_url(self):
        return reverse_lazy('Inicio:index')

COR = (
    ('CINZA', 'cinza'),
    ('VERDE', 'verde'),
)

class Cargas(models.Model):

    Carga_Placa = models.ForeignKey(Caminhao, on_delete=models.CASCADE, null=True, blank=True,related_name="carga_placa")  # One-to-one relationship
    data = models.DateTimeField('criado em',auto_now_add=True,auto_now=False )
    p2 = models.IntegerField(default=0,blank=True, null=True)
    p5 = models.IntegerField(default=0,blank=True, null=True)
    p8 = models.IntegerField(default=0,blank=True, null=True)
    p13 = models.IntegerField(default=0,blank=True, null=True)
    p20 = models.IntegerField(default=0,blank=True, null=True)
    p45 = models.IntegerField(default=0,blank=True, null=True)
    cor = models.CharField(max_length=5, choices=COR, blank=True)

    def __str__(self):
        return self.data
    class Meta:
        ordering = ('-data',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(Cargas)
        permission = Permission.objects.filter(content_type=content_type, codename=['administrativo','frota'])
        return permission
    def get_absolute_url(self):
        return reverse_lazy('administrativo:fornulario_lista')



class Abastecimento(models.Model):
    Nome_motorista = models.ForeignKey(Motorista,on_delete=models.CASCADE, null=False, blank=False,related_name="Nome_motoristas")
    km = models.IntegerField(default=0,null=False, blank=False)
    horimetro=models.IntegerField(default=0,null=False, blank=False)
    Litros = models.IntegerField(default=0,null=False, blank=False)
    hodometro=models.IntegerField(default=0,null=False, blank=False)
    data = models.DateField('criado em',auto_now_add=True,auto_now=False )
    hora = models.TimeField('criado em',auto_now_add=True,auto_now=False,max_length=5 )
    Abastecimento_placa = models.ForeignKey(Caminhao, on_delete=models.CASCADE,null=False, blank=False,related_name="abastecimento_pĺacas")
    responsave_abastecimento = models.CharField(max_length=30,null=False, blank=False)
    def __str__(self):
        return '{}-{}-{}'.format(self.responsave_abastecimento, self.Nome_motorista,self.Abastecimento_placa)
    class Meta:
        ordering = ('data',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(Abastecimento)
        permission = Permission.objects.filter(content_type=content_type, codename=['administrativo','frota','abastecimento'])
        return permission
    def get_absolute_url(self):
        return reverse_lazy('abastecimento:abastecimento')
    
equipamentos = (
    ('LUVA', 'luva'),
    ('CAPACETE', 'capacete'),
    ('OCLULOS', 'oculos'),
    ('PROTETOR DE OUVIDO', 'protetor de ouvido'),
    ('PROTETOR SOLAR', 'protetor solar'),
)

class epis_base(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name="epis")
    data = models.DateField('criado em',auto_now_add=True,auto_now=False )
    horario = models.TimeField('criado em',auto_now_add=True,auto_now=False )
    epis =  models.CharField(max_length=30,choices=equipamentos, blank=True,null=True)

    def __str__(self):
        return '{}-{}'.format(self.data, self.epis)
    class Meta:
        ordering = ('-data',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(epis_base)
        permission = Permission.objects.filter(content_type=content_type, codename=['administrativo','frota','manutencao','abastecimento'])
        return permission
    def get_absolute_url(self):
        return reverse_lazy('Inicio:index')

uniformes_tipo= (
    ('CAMISA','camisa'),
    ('CALÇA','calça'),
    ('BOTA','bota'),
    ('BONÉ','boné'),
)
class uniformes_base(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name="uniformes")
    data = models.DateField('criado em',auto_now_add=True,auto_now=False )
    horario = models.TimeField('criado em',auto_now_add=True,auto_now=False )
    tipo =  models.CharField(max_length=30,choices=uniformes_tipo, blank=True,null=True)
    tamanho = models.CharField('tamanho',max_length=20,blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.data, self.tipo)
    class Meta:
        ordering = ('-data',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(uniformes_base)
        permission = Permission.objects.filter(content_type=content_type, codename=['administrativo','frota','manutencao','abastecimento'])
        return permission
    def get_absolute_url(self):
        return reverse_lazy('Inicio:index')
    
class outros_base(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name="outros")
    data = models.DateField('criado em',auto_now_add=True,auto_now=False )
    horario = models.TimeField('criado em',auto_now_add=True,auto_now=False )
    outros = models.CharField('outros',max_length=20,blank=True, null=True)
    texto= models.TextField('Motivo',blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.data, self.outros)
    class Meta:
        ordering = ('-data',)

    def permission(self):
        content_type = ContentType.objects.get_for_model(outros_base)
        permission = Permission.objects.filter(content_type=content_type, codename=['administrativo','frota','manutencao','abastecimento'])
        return permission
    def get_absolute_url(self):
        return reverse_lazy('Inicio:index')