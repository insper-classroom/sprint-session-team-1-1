from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # Classe que já vem com o Django para criar um formulário de registro de usuários
from .models import Profile

class UserForm(UserCreationForm):
    # username não precisa ser obrigatório
    username = forms.CharField(max_length=100, required=False) # O campo username não é obrigatório
    email = forms.EmailField(max_lengh=100, required=True) # O campo email é obrigatório
    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput) # O campo password1 é obrigatório
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput) # O campo password2 é obrigatório
    nome_completo = forms.CharField(max_length=150, required=True) # O campo nome_completo é obrigatório
    data_nascimento = forms.DateField(required=True) # O campo data_nascimento é obrigatório
    cpf = forms.CharField(max_length=14, required=True) # O campo cpf é obrigatório
    rg = forms.CharField(max_length=12, required=True) # O campo rg é obrigatório
    telefone = forms.CharField(max_length=15, required=True) # O campo telefone é obrigatório
    genero = forms.CharField(max_length=20, required=True) # O campo genero é obrigatório
    outro_genero = forms.CharField(max_length=100, required=False) # O campo outro_genero não é obrigatório
    cor_ou_raca = forms.CharField(max_length=20, required=True) # O campo cor_ou_raca é obrigatório
    outra_cor_ou_raca = forms.CharField(max_length=100, required=False) # O campo outra_cor_ou_raca não é obrigatório

    class Meta:
        model = User # O modelo é o User
        fields = [
        'username',
        'email',
        'password1',
        'password2',
        'nome_completo',
        'data_nascimento',
        'cpf',
        'rg',
        'telefone',
        'genero',
        'outro_genero',
        'cor_ou_raca',
        'outra_cor_ou_raca',
        ] # Campos que serão exibidos no formulário de registro

    def save(self, commit=True): # Sobrescrevemos o método save para adicionar o email ao usuário
        user = super(UserForm, self).save(commit=False) # Chamamos o método save da classe UserCreationForm
        user.email = self.cleaned_data['email'] # Adicionamos o email ao usuário
        if commit:
            user.save() # Salvamos o usuário
            Profile.objects.create(
                usuario=user, 
                email=user.email,
                nome_exibicao=user.username,
                nome_completo=self.cleaned_data['nome_completo'],
                data_nascimento=self.cleaned_data['data_nascimento'],
                cpf=self.cleaned_data['cpf'],
                rg=self.cleaned_data['rg'],
                telefone=self.cleaned_data['telefone'],
                genero=self.cleaned_data['genero'],
                outro_genero=self.cleaned_data['outro_genero'],
                cor_ou_raca=self.cleaned_data['cor_ou_raca'],
                outra_cor_ou_raca=self.cleaned_data['outra_cor_ou_raca'],
            ) # Criamos um objeto do tipo Profile ligado ao usuário
            
        return user # Retornamos o usuário