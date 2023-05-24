from typing import Any, Dict
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


# Create your views here.

# Aqui nas views, teremos o cadastro de usuários
class UserCreate(CreateView):
    # template_name = ""
    form_class = forms.UserForm # Aqui, definimos o formulário que será usado para o cadastro de usuários
    # success_url = reverse_lazy('login') # Aqui, definimos a URL para onde o usuário será redirecionado após o cadastro

    def get_context_data(self, *args, **kwargs): # Sobrescrevemos o método get_context_data para adicionar mais campos ao contexto
        context = super().get_context_data(*args, **kwargs)

        # Aqui, adicionamos os campos do Profile ao contexto para que possam ser preenchidos pelo usuário
        context['nome_completo'] = self.request.POST.get('nome_completo')
        context['email'] = self.request.POST.get('email')
        context['nome_exibicao'] = self.request.POST.get('nome_exibicao')
        context['data_nascimento'] = self.request.POST.get('data_nascimento')
        context['cpf'] = self.request.POST.get('cpf')
        context['rg'] = self.request.POST.get('rg')
        context['telefone'] = self.request.POST.get('telefone')
        context['genero'] = self.request.POST.get('genero')
        context['outro_genero'] = self.request.POST.get('outro_genero')
        context['cor_ou_raca'] = self.request.POST.get('cor_ou_raca')
        context['outra_cor_ou_raca'] = self.request.POST.get('outra_cor_ou_raca')
        
        return context
    
def signup(request):
    
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = forms.UserForm()
    return render(request, 'users/signup.html', {'form': form})