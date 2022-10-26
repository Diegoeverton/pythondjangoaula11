from importlib.metadata import files
from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from viagens.classe_viagem import tipos_de_classe
from viagens.validar import *
from viagens.models import Viagem, ClasseViagem, Pessoa



class ViagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa',disabled=True, initial=datetime.today)

    class Meta:
        model = Viagem
        fields = '__all__'
        labels = {'data_ida':'Data de ida', 'data_volta': 'Data de volta', 'informacoes':'informacoes', 'classe_viagem':'Tipo de voo'}
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']


   
    
   
   

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('Data_pesquisa')
        
        listaErros = {}
        campo_temNumero(origem, 'origem', listaErros)
        campo_temNumero(destino, 'destino', listaErros)
        origem_destino_iguais(origem, destino, listaErros)
        if listaErros is not None:
            for erro in listaErros:
                mensagem_erro = listaErros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data
    

