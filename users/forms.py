from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # Classe que já vem com o Django para criar um formulário de registro de usuários
from .models import Profile

class UserForm(UserCreationForm):

    #Formulario base
    username = forms.CharField(max_length=100, required=True) # O campo username não é obrigatório
    email = forms.EmailField(max_length=100, required=True) # O campo email é obrigatório
    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput) # O campo password1 é obrigatório
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput) # O campo password2 é obrigatório
    nome_completo = forms.CharField(max_length=150, required=True) # O campo nome_completo é obrigatório
    #Cria o campo data de nascimento. Ocupa muito espaço pois deixo o formato dd/mm/yyyy por padrao, au invez do mm/dd/yyyy default.
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True) # O campo data_nascimento é obrigatório
    cpf = forms.CharField(max_length=14, required=True) # O campo cpf é obrigatório
    rg = forms.CharField(max_length=12, required=True) # O campo rg é obrigatório
    telefone = forms.CharField(max_length=19, required=True) # O campo telefone é obrigatório
    genero = forms.ChoiceField(choices=Profile.Genders, required=True) # O campo genero é obrigatório
    outro_genero = forms.CharField(max_length=100, required=False) # O campo outro_genero não é obrigatório
    cor_ou_raca = forms.ChoiceField(choices=Profile.Race, required=True) # O campo cor_ou_raca é obrigatório
    outra_cor_ou_raca = forms.CharField(max_length=100, required=False) # O campo outra_cor_ou_raca não é obrigatório
    estado_nascimento= forms.ChoiceField(choices=Profile.cities_test, required=True) # O campo cor_ou_raca é obrigatório
    cidade_nascimento = forms.ChoiceField(choices=Profile.cities_test, required=True) # O campo cor_ou_raca é obrigatório
    pais_atual = forms.ChoiceField(choices=Profile.cities_test, required=True) # O campo cor_ou_raca é obrigatório
    estado_atual = forms.ChoiceField(choices=Profile.cities_test, required=False) # O campo cor_ou_raca é obrigatório
    cidade_atual = forms.ChoiceField(choices=Profile.cities_test, required=False) # O campo cor_ou_raca é obrigatório
    cidade_fora_atual = forms.CharField(max_length=100, required=False) # O campo cor_ou_raca é obrigatório
    linkedin = forms.CharField(max_length=100, required=False) # O campo cor_ou_raca é obrigatório
    tipo_usuario = forms.ChoiceField(choices=Profile.User_type, initial='Bolsista', required=True) # O campo cor_ou_raca é obrigatório
    faculdade = forms.ChoiceField(choices=Profile.University, required=True) # O campo cor_ou_raca é obrigatório
    curso = forms.CharField(max_length=100, required=True) # O campo cor_ou_raca é obrigatório
    ano_ingresso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True) # O campo data_nascimento é obrigatório
    ano_formatura = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True) # O campo data_nascimento é obrigatório
    renda_familiar = forms.ChoiceField(choices=Profile.Income, required=True) # O campo cor_ou_raca é obrigatório


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
        'estado_nascimento',
        'cidade_nascimento',
        'pais_atual',
        'estado_atual',
        'cidade_atual',
        'cidade_fora_atual',
        'linkedin',
        'faculdade',
        'curso',
        'ano_ingresso',
        'ano_formatura',
        'renda_familiar',
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
                estado_nascimento=self.cleaned_data['estado_nascimento'],
                cidade_nascimento=self.cleaned_data['cidade_nascimento'],
                pais_atual=self.cleaned_data['pais_atual'],
                estado_atual=self.cleaned_data['estado_atual'],
                cidade_atual=self.cleaned_data['cidade_atual'],
                cidade_fora_atual=self.cleaned_data['cidade_fora_atual'],
                linkedin=self.cleaned_data['linkedin'],
                tipo_usuario=self.cleaned_data['tipo_usuario'],
                faculdade=self.cleaned_data['faculdade'],
                curso=self.cleaned_data['curso'],
                ano_ingresso=self.cleaned_data['ano_ingresso'],
                ano_formatura=self.cleaned_data['ano_formatura'],
                renda_familiar=self.cleaned_data['renda_familiar'],
            ) # Criamos um objeto do tipo Profile ligado ao usuário
            
        return user # Retornamos o usuário
    
    #Código feito pelo chatGPT para em conjunto do código em JS tornar os campos outra raça e outro genero visiveis apenas caso selecione-se a opção outro.
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['tipo_usuario'].widget = forms.HiddenInput()  #Esconde o campo "Tipo_usuario", por padrao sempre sera bolsista.
            if 'genero' in self.data and self.data['genero'] == 'Outro':
                self.fields['outro_genero'].required = True
                self.fields['outro_genero'].widget.attrs['style'] = '' #Torna visivel
            if 'cor_ou_raca' in self.data and self.data['cor_ou_raca'] == 'Outra':
                self.fields['outra_cor_ou_raca'].required = True
                self.fields['outra_cor_ou_raca'].widget.attrs['style'] = '' #Torna visivel