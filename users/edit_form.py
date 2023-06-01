from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class EditForm(UserChangeForm):
    nome = forms.CharField(max_length=150, required=True) # O campo nome_completo é obrigatório
    sobrenome = forms.CharField(max_length=150, required=True) # O campo nome_completo é obrigatório
    username = forms.CharField(max_length=100, required=True) # O campo username não é obrigatório
    email = forms.EmailField(max_length=100, required=True) # O campo email é obrigatório
    #Foto de perfil
    foto_perfil = forms.ImageField(required=False)
    #Cria o campo data de nascimento. Ocupa muito espaço pois deixo o formato dd/mm/yyyy por padrao, au invez do mm/dd/yyyy default.
    rg = forms.CharField(max_length=12, required=True) # O campo rg é obrigatório
    telefone = forms.CharField(max_length=19, required=True) # O campo telefone é obrigatório
    genero = forms.ChoiceField(choices=Profile.Genders, required=True) # O campo genero é obrigatório
    outro_genero = forms.CharField(max_length=100, required=False) # O campo outro_genero não é obrigatório
    pais_atual = forms.ChoiceField(choices=Profile.cities_test, required=True) # O campo cor_ou_raca é obrigatório
    estado_atual = forms.ChoiceField(choices=Profile.cities_test, required=False) # O campo cor_ou_raca é obrigatório
    cidade_atual = forms.ChoiceField(choices=Profile.cities_test, required=False) # O campo cor_ou_raca é obrigatório
    cidade_fora_atual = forms.CharField(max_length=100, required=False) # O campo cor_ou_raca é obrigatório
    linkedin = forms.CharField(max_length=100, required=False) # O campo cor_ou_raca é obrigatório
    curso = forms.CharField(max_length=100, required=True) # O campo cor_ou_raca é obrigatório
    ano_formatura = forms.CharField(max_length=4, required=True) # O campo rg é obrigatório
    renda_familiar = forms.ChoiceField(choices=Profile.Income, required=True) # O campo cor_ou_raca é obrigatório


    class Meta:
        model = User
        fields = [
            'nome',
            'sobrenome',
            'username',
            'email',
            'foto_perfil',
            'rg',
            'telefone',
            'genero',
            'outro_genero',
            'pais_atual',
            'estado_atual',
            'cidade_atual',
            'cidade_fora_atual',
            'linkedin',
            'curso',
            'ano_formatura',
            'renda_familiar',
        ]