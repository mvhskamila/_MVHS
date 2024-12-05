from django import forms

from db_mvhs.models import *

class forms_caminhao(forms.ModelForm):

    class Meta:
        model = Caminhao
        fields = '__all__'


class forms_Motorista(forms.ModelForm):

    class Meta:
        model = Motorista
        fields = '__all__'

class forms_Ajudante(forms.ModelForm):

    class Meta:
        model = Ajudante
        fields = '__all__'

class forms_td(forms.ModelForm):

    class Meta:
        model = tab_td
        fields = '__all__'




class forms_revenda(forms.ModelForm):

    class Meta:
        model = Revenda
        fields = '__all__'

class forms_manutencao(forms.ModelForm):

    class Meta:
        model = Manutencao
        fields = '__all__'


class forms_Manutencao_Resposta(forms.ModelForm):

    class Meta:
        model = Manutencao_Resposta
        fields = '__all__'

class forms_Cargas(forms.ModelForm):

    class Meta:
        model = Cargas
        fields = '__all__'

class forms_Abastecimento(forms.ModelForm):

    class Meta:
        model = Abastecimento
        fields = '__all__'

class forms_uniformes(forms.ModelForm):

    class Meta:
        model = uniformes_base
        fields = '__all__'

class forms_epis(forms.ModelForm):

    class Meta:
        model = epis_base
        fields = '__all__'

class forms_outros(forms.ModelForm):

    class Meta: 
        model = outros_base
        fields = '__all__'  
    