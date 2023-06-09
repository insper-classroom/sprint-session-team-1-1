from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from users.models import HistoricoAcademico
from users.models import HistoricoProfissional
from .filters import apply_filters
from .charts import *


# Create your views here.
@login_required
def individual_table(request):
    user = request.user
    profile = user.profile 
    if profile.tipo_usuario != 'Colaborador' and profile.tipo_usuario != 'Admin':
        return redirect('/')
    else:
        all_users = User.objects.all().order_by('-date_joined')
        filtered_users = apply_filters(all_users, request)
        return render(request, 'search/search.html', {'users': filtered_users})
    

@login_required
def profile_id(request, user_id):
    if request.user.profile.tipo_usuario != 'Colaborador' and request.user.profile.tipo_usuario != 'Administrador':
        return redirect('/')
    else:
        user = User.objects.get(id = user_id)
        profile = user.profile  # Certifique-se de ter um relacionamento correto entre os modelos User e Profile
        img = profile.foto_perfil
        path_image = "/".join(str(img).split('/')[2:])

        # Verificar o tipo de usuário com base na data de formatura e no ano atual (SEMPRE QUANDO ENTRAR NO PRÓPRIO PERFIL)
        # Assim o estado de Bolsista ou Alumni SEMPRE sera atualizado
        if profile.tipo_usuario != 'Admin' and profile.tipo_usuario != 'Sponsor' and profile.tipo_usuario != 'Colaborador':
            ano_formatura = profile.ano_formatura
            ano_atual = datetime.now().year
            profile.tipo_usuario = 'Bolsista' if int(ano_formatura) > ano_atual else 'Alumni'
            profile.save()

        return render(request, 'search/profile-visitor.html', {'user': user, 'path_image': path_image,})
    

# Função responsavel pela criação de gráficos
@login_required
def charts(request):
    user = request.user
    profile = user.profile 
    if profile.tipo_usuario != 'Colaborador' and profile.tipo_usuario != 'Admin' and profile.tipo_usuario != 'Sponsor':
        return redirect('/')
    else:
        #Filtra os usuarios
        all_users = User.objects.filter(profile__tipo_usuario__in=["Bolsista", "Alumni"]).order_by('-date_joined')
        filtered_users = apply_filters(all_users, request)

        #Cria os graficos a partir das funções no charts.py, separei por questão de organização
        grafico_cor = cria_grafico_cor_ou_raca(filtered_users)
        grafico_genero = cria_grafico_genero(filtered_users)
        grafico_tipo_usuario = cria_grafico_tipo_usuario(filtered_users)
        grafico_faculdade = cria_grafico_faculdade(filtered_users)
        grafico_renda = cria_grafico_renda(filtered_users)
        grafico_estado_nascimento = cria_grafico_estado_nascimento(filtered_users)
        grafico_pais_atual = cria_grafico_pais_atual(filtered_users)
        grafico_estado_atual = cria_grafico_estado_atual(filtered_users)

        graphs = {
            'cor_ou_raca': grafico_cor,
            'genero': grafico_genero,
            'tipo_usuario': grafico_tipo_usuario,
            'faculdade': grafico_faculdade,
            'renda': grafico_renda,
            'estado_nascimento': grafico_estado_nascimento,
            'pais_atual': grafico_pais_atual,
            'estado_atual': grafico_estado_atual
        }
        return render(request, 'search/overview.html', {'users': filtered_users, 'graphs': graphs, 'profile': profile})


@login_required
def history_id_academic(request, user_id):
    if request.user.profile.tipo_usuario != 'Colaborador' and request.user.profile.tipo_usuario != 'Administrador':
        return redirect('/')
    else:
        user = User.objects.get(id = user_id)
        historicos_academicos = HistoricoAcademico.objects.all().order_by('-criado_em')
        return render(request, 'search/historico-academico-visitor.html', {'historicos': historicos_academicos, 'user': user})
    
@login_required
def history_id_professional(request, user_id):
    if request.user.profile.tipo_usuario != 'Colaborador' and request.user.profile.tipo_usuario != 'Administrador':
        return redirect('/')
    else:
        user = User.objects.get(id = user_id)
        historicos_profissionais = HistoricoProfissional.objects.all().order_by('-criado_em')
        return render(request, 'search/historico-profissional-visitor.html', {'historicos': historicos_profissionais, 'user': user})