# Register your models here.
from django.contrib import admin
from db_mvhs.models import *
# Register your models here.

@admin.register(Caminhao)
class caminhaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('placa_veiculo',)

@admin.register(tab_td)
class tab_tdAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('td',)

@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('motorista',)

@admin.register(Ajudante)
class AjudanteAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('Ajudante',)

@admin.register(Revenda)
class RevendaAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('placa_veiculo',)

@admin.register(Manutencao)
class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('responsavel',)

@admin.register(Manutencao_Resposta)
class Manutencao_RespostaAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('Agendado',)

@admin.register(Abastecimento)
class AbastecimentoAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('data',)
@admin.register(epis_base)
class epis_baseAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('data',)

@admin.register(outros_base)
class outros_baseAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('data',)   

@admin.register(uniformes_base)
class uniformes_baseAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('data',)