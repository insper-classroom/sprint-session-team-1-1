import random

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .models import HistoricoAcademico
from .models import HistoricoProfissional
from datetime import datetime
from .forms import UserForm
from .models import Keys
from . import edit_form
from . import forms


def home(request):
    return render(request, 'home-page/home.html')


class UserCreate(CreateView):
    form_class = forms.UserForm # Aqui, definimos o formulário que será usado para o cadastro de usuários
    success_url = reverse_lazy('home') # Aqui, definimos a URL para onde o usuário será redirecionado após o cadastro

    def get_context_data(self, *args, **kwargs): # Sobrescrevemos o método get_context_data para adicionar mais campos ao contexto
        context = super().get_context_data(*args, **kwargs)
        # Aqui, adicionamos os campos do Profile ao contexto para que possam ser preenchidos pelo usuário
        context['nome'] = self.request.POST.get('nome')
        context['sobrenome'] = self.request.POST.get('sobrenome')
        context['email'] = self.request.POST.get('email')
        context['foto_perfil'] = self.request.POST.get('foto_perfil')
        context['nome_exibicao'] = self.request.POST.get('nome_exibicao')
        context['data_nascimento'] = self.request.POST.get('data_nascimento')
        context['cpf'] = self.request.POST.get('cpf')
        context['rg'] = self.request.POST.get('rg')
        context['telefone'] = self.request.POST.get('telefone')
        context['genero'] = self.request.POST.get('genero')
        context['outro_genero'] = self.request.POST.get('outro_genero')
        context['cor_ou_raca'] = self.request.POST.get('cor_ou_raca')
        context['outra_cor_ou_raca'] = self.request.POST.get('outra_cor_ou_raca')
        context['estado_nascimento'] = self.request.POST.get('estado_nascimento')
        context['cidade_nascimento'] = self.request.POST.get('cidade_nascimento')
        context['pais_atual'] = self.request.POST.get('pais_atual')
        context['estado_atual'] = self.request.POST.get('estado_atual')
        context['cidade_atual'] = self.request.POST.get('cidade_atual')
        context['cidade_fora_atual'] = self.request.POST.get('cidade_fora_atual')
        context['linkedin'] = self.request.POST.get('linkedin')
        context['faculdade'] = self.request.POST.get('faculdade')
        context['curso'] = self.request.POST.get('curso')
        context['ano_ingresso'] = self.request.POST.get('ano_ingresso')
        context['ano_formatura'] = self.request.POST.get('ano_formatura')
        context['renda_familiar'] = self.request.POST.get('renda_familiar')
        
        return context
    
    def form_valid(self, form):
        # Determinar o tipo de usuário com base na data de formatura
        ano_formatura = form.instance.ano_formatura
        ano_atual = datetime.datetime.now().year
        tipo_usuario = 'Aluno' if int(ano_formatura) > ano_atual else 'Alumni'
        form.instance.tipo_usuario = tipo_usuario
        return super().form_valid(form)

@login_required
def profile(request):
    user = request.user
    profile = user.profile  # Certifique-se de ter um relacionamento correto entre os modelos User e Profile
    img = profile.foto_perfil
    img_user = "/".join(str(img).split('/')[2:])

    # Verificar o tipo de usuário com base na data de formatura e no ano atual (SEMPRE QUANDO O USUÁRIO ENTRAR NO PRÓPRIO PERFIL)
    if profile.tipo_usuario != 'Admin' and profile.tipo_usuario != 'Sponsor' and profile.tipo_usuario != 'Colaborador':
        ano_formatura = profile.ano_formatura
        ano_atual = datetime.now().year
        profile.tipo_usuario = 'Bolsista' if int(ano_formatura) > ano_atual else 'Alumni'
        profile.save()

    return render(request, 'profile/profile.html', {'user': user, 'img_user': img_user})


def custom_logout(request):
    logout(request)
    # Redirecionar para a página desejada após o logout
    return redirect('home')


# Função que gera uma key unica para ser usada no signup do usuario
def gerador():
    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
    key = ""

    for i in range(50):
        indice = random.randint(0, len(caracteres)-1) # Gera um índice aleatório
        key += caracteres[indice]  # Concatena o caractere correspondente ao índice na chave

    return key


def redirect_home(request):
    return redirect('/')


@login_required
def generate_link(request):
    user = request.user
    if user.profile.tipo_usuario == 'Admin' or user.profile.tipo_usuario == 'Colaborador':
        key = gerador()
        key_obj = Keys(key=key) 
        key_obj.save() # Salvando a chave no banco de dados
        return render(request, 'search/generate_link.html', {'key': key})
        # return HttpResponse(f"<h1>localhost:8000/accounts/signup/{key}</h1>")
    else:
        return redirect('/')


# Signup 2.0, a função foi refeita usando a primeira de base para agora suportar o link gerado aleatoriamente.
def signup(request, key):
    lista_keys = Keys.objects.all()
    for ativa in lista_keys:
        if key == ativa.key:  # Verifique se a chave corresponde à chave no objeto
            if request.method == 'POST':
                form = forms.UserForm(request.POST, request.FILES)
                if form.is_valid():
                    user = form.save()

                    #Cadastra o usuario como Bolsista ou Alumni baseado no ano de formatura
                    profile = user.profile
                    ano_formatura = profile.ano_formatura
                    ano_atual = datetime.now().year
                    profile.tipo_usuario = 'Bolsista' if int(ano_formatura) > ano_atual else 'Alumni'
                    profile.save()


                    group_names = list(Group.objects.values_list('name', flat=True))
                    if 'bolsista' not in group_names:
                        bolsista = Group(name='bolsista')
                        bolsista.save()
                    else:   
                        bolsista = Group.objects.get(name='bolsista')
                    user.groups.add(bolsista)
                    # Excluir a chave
                    ativa.delete()
                    return redirect('/accounts/login/')       
            else:
                form = UserForm()
            return render(request, 'users/signup.html', {'form': form})
    return redirect('/')


#Código para edição de usuario
@login_required
def edit(request):
    user = request.user
    profile = user.profile
    img = profile.foto_perfil
    img_user = "/".join(str(img).split('/')[2:])

    if request.method == 'POST':
        username_old = user.username
        form = edit_form.EditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            #Este pedaço dividido foi feito com a ajuda do chatGPT, pois estavamos com dificuldade de fazer a validação de username
            #Mas entendemos o conceito de utilizar a personal key para liberar a 'edição' para um username ja existente caso seja do msm usuario
            if form.cleaned_data['username'] != username_old:
                new_username = form.cleaned_data['username']
                existing_user = User.objects.filter(username=new_username).exclude(pk=user.pk).exists()
                if not existing_user:
                    user.username = new_username
                    profile.nome_exibicao = new_username
                else:
                    form.add_error('username', 'A user with that username already exists.')
            # Determinar o tipo de usuário com base na data de formatura
            if profile.tipo_usuario != 'Admin' and profile.tipo_usuario != 'Sponsor' and profile.tipo_usuario != 'Colaborador':
                ano_formatura = int(form.cleaned_data['ano_formatura'])
                ano_atual = datetime.now().year
                tipo_usuario = 'Bolsista' if ano_formatura > ano_atual else 'Alumni'
                profile.tipo_usuario = tipo_usuario

            user.first_name = form.cleaned_data['nome']
            user.last_name = form.cleaned_data['sobrenome']
            user.email = form.cleaned_data['email']
            profile.nome = form.cleaned_data['nome']
            profile.sobrenome = form.cleaned_data['sobrenome']
            profile.email = form.cleaned_data['email']
            #Código para só atualizar a foto se uma nova for enviada
            if request.FILES.get('foto_perfil') != None:
                profile.foto_perfil = request.FILES.get('foto_perfil')

            profile.rg = form.cleaned_data['rg']
            profile.telefone = form.cleaned_data['telefone']
            profile.genero = form.cleaned_data['genero']
            profile.outro_genero = form.cleaned_data['outro_genero']
            profile.pais_atual = form.cleaned_data['pais_atual']
            profile.estado_atual = form.cleaned_data['estado_atual']
            profile.cidade_atual = form.cleaned_data['cidade_atual']
            profile.cidade_fora_atual = form.cleaned_data['cidade_fora_atual']
            profile.linkedin = form.cleaned_data['linkedin']
            profile.curso = form.cleaned_data['curso']
            profile.ano_formatura = form.cleaned_data['ano_formatura']
            profile.renda_familiar = form.cleaned_data['renda_familiar']

            profile.save()
            user.save()
            return redirect('/accounts/profile/')
        
    else:
        #Listamos todos os fields e auto preenchemos com os valores ja existentes do usuario
        form = edit_form.EditForm(initial={
            'nome': user.first_name,
            'sobrenome': user.last_name,
            'username': user.username,
            'email': user.email,
            'foto_perfil': user.profile.foto_perfil,
            'rg': user.profile.rg,
            'telefone': user.profile.telefone,
            'genero': user.profile.genero,
            'outro_genero': user.profile.outro_genero,
            'pais_atual': user.profile.pais_atual,
            'estado_atual': user.profile.estado_atual,
            'cidade_atual': user.profile.cidade_atual,
            'cidade_fora_atual': user.profile.cidade_fora_atual,
            'linkedin': user.profile.linkedin,
            'curso': user.profile.curso,
            'ano_formatura': user.profile.ano_formatura,
            'renda_familiar': user.profile.renda_familiar,
        })

        #Validador personalizado feito com auxilio do ChatGPT
        form.fields['username'].validators.append(UnicodeUsernameValidator())

    return render(request, 'profile/edit/edit.html', {'form': form, 'user': user, 'img_user': img_user})


@login_required
def historico_academico(request):
    user= request.user
    if request.method == 'POST':
        form_academico = forms.HistoricoAcademicoForm(request.POST, request.FILES)
        if form_academico.is_valid():
            form_academico.save()
        return redirect('/accounts/profile/history/academic')

    else:
        form_academico = forms.HistoricoAcademicoForm(initial={'id_proprietario': user.id})
        historicos_academicos = HistoricoAcademico.objects.all().order_by('-criado_em')
        return render(request, 'history/historico-academico.html', {'form_academico': form_academico, 'historicos': historicos_academicos, 'user': user})
    

@login_required
def historico_profissional(request):
    user= request.user
    if request.method == 'POST':
        form_profissional = forms.HistoricoProfissionalForm(request.POST, request.FILES)
        if form_profissional.is_valid():
            form_profissional.save()
        return redirect('/accounts/profile/history/professional')

    else:
        form_profissional = forms.HistoricoProfissionalForm(initial={'id_proprietario': user.id})
        historicos_profissionais = HistoricoProfissional.objects.all().order_by('-criado_em')
        return render(request, 'history/historico-profissional.html', {'form_profissional': form_profissional, 'historicos': historicos_profissionais, 'user': user})
