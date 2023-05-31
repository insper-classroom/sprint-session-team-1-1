from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserForm
from django.urls import reverse_lazy
from datetime import datetime


# Create your views here.

# Aqui nas views, teremos o cadastro de usuários
class UserCreate(CreateView):
    # template_name = ""
    form_class = forms.UserForm # Aqui, definimos o formulário que será usado para o cadastro de usuários
    success_url = reverse_lazy('home') # Aqui, definimos a URL para onde o usuário será redirecionado após o cadastro

    def get_context_data(self, *args, **kwargs): # Sobrescrevemos o método get_context_data para adicionar mais campos ao contexto
        context = super().get_context_data(*args, **kwargs)

        # Aqui, adicionamos os campos do Profile ao contexto para que possam ser preenchidos pelo usuário
        context['nome'] = self.request.POST.get('nome')
        context['sobrenome'] = self.request.POST.get('sobrenome')
        context['email'] = self.request.POST.get('email')
        context['nome_exibicao'] = self.request.POST.get('nome_exibicao')
        context['foto_de_perfil'] = self.request.POST.get('foto_de_perfil')
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


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile/profile.html', {'user': request.user})


def custom_logout(request):
    logout(request)
    # Redirecionar para a página desejada após o logout
    return redirect('home')


@login_required
def edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts/profile')
    else:
        form = UserForm(instance=profile)
    context = {'form': form}
    return render(request, 'users/signup.html', context)