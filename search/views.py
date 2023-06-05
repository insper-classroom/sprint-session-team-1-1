from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from .filters import apply_filters
import matplotlib.pyplot as plt
import io
import urllib, base64




# Create your views here.
@login_required
def individual_table(request):
    user = request.user
    profile = user.profile 
    if profile.tipo_usuario != 'Colaborador' and profile.tipo_usuario != 'Admin':
        return redirect('/')
    else:
        all_users = User.objects.all().order_by('-date_joined')
        # for user in all_users:
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
    
def charts(request):
    # Recupere as informações dos usuários bolsistas
    bolsistas = User.objects.filter(profile__tipo_usuario='Bolsista')
    
    # Crie os dados para o gráfico
    # Exemplo: Contagem de bolsistas por área de estudo
    faculdades = [b.profile.faculdade for b in bolsistas]
    contagem_faculs = {}
    for area in faculdades:
        if area in contagem_faculs:
            contagem_faculs[area] += 1
        else:
            contagem_faculs[area] = 1
    
    
    plt.bar(contagem_faculs.keys(), contagem_faculs.values())
    plt.xlabel('Faculdade')
    plt.ylabel('Número de Bolsistas')
    plt.title('Contagem de Bolsistas por Área de Estudo')
    

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    # Renderize a página com o gráfico
    return render(request, 'search/overview.html', {'graficos': image_base64})