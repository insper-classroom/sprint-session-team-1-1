from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from .filters import apply_filters
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('Agg')
import io
import urllib, base64




# Create your views here.
@login_required
def individual_table(request):
    user = request.user
    profile = user.profile 
    # if profile.tipo_usuario != 'Colaborador' and profile.tipo_usuario != 'Admin':
    #     return redirect('/')
    # else:
    all_users = User.objects.all().order_by('-date_joined')
    # for user in all_users:
    filtered_users = apply_filters(all_users, request)
    return render(request, 'search/search.html', {'users': filtered_users})
    

@login_required
def profile_id(request, user_id):
    # if request.user.profile.tipo_usuario != 'Colaborador' and request.user.profile.tipo_usuario != 'Administrador':
    #     return redirect('/')
    # else:
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
    
    # Gráfico 1: Contagem de bolsistas por faculdade
    faculdades = [b.profile.faculdade for b in bolsistas]
    contagem_faculdades = {}
    for faculdade in faculdades:
        if faculdade in contagem_faculdades:
            contagem_faculdades[faculdade] += 1
        else:
            contagem_faculdades[faculdade] = 1
    
    
    plt.bar(contagem_faculdades.keys(), contagem_faculdades.values())
    plt.xlabel('Faculdade')
    plt.ylabel('Número de Bolsistas')
    plt.title('Contagem de Bolsistas por Faculdade')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_faculdades = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    # Gráfico 2: Contagem de bolsistas por curso
    cursos = [b.profile.curso for b in bolsistas]
    contagem_cursos = {}
    for curso in cursos:
        if curso in contagem_cursos:
            contagem_cursos[curso] += 1
        else:
            contagem_cursos[curso] = 1
    

    plt.bar(contagem_cursos.keys(), contagem_cursos.values())
    plt.xlabel('Curso')
    plt.ylabel('Número de Bolsistas')
    plt.title('Contagem de Bolsistas por Curso')
    
    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    grafico_cursos = base64.b64encode(buffer2.getvalue()).decode()
    plt.close()
    
    graficos = {'graficos_faculdades': grafico_faculdades, 'graficos_cursos': grafico_cursos}
    
    # Renderize a página com os gráficos
    return render(request, 'search/overview.html', {'graficos': graficos})