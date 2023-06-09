import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import urllib, base64

#Variavel global com todas as cores para serem usadas nos graficos, em ordem
cores = ['#3C5AF0', '#FAC800', '#64B100', 'orange', 'red', 'pink', 'lightblue', 'lime', 'purple', 'gray']


def cria_grafico_cor_ou_raca(filtered_users):
    # Grafico usuarios por cor ou raça
    cor_raca = {}
    for fuser in filtered_users:
        if fuser.profile.cor_ou_raca not in cor_raca:
            cor_raca[fuser.profile.cor_ou_raca] = 1
        else:
            cor_raca[fuser.profile.cor_ou_raca] += 1

    labels = list(cor_raca.keys())
    n_pessoas = list(cor_raca.values())
    labels_with_count = ['{} ({})'.format(label, count) for label, count in zip(labels, n_pessoas)]

    plt.figure(figsize=(8, 6))
    plt.pie(n_pessoas, labels=labels_with_count, autopct='%.2f%%', counterclock=False, startangle=90, colors=cores)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_cor = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return grafico_cor

def cria_grafico_genero(filtered_users):
    # Grafico usuarios por genero
    genero = {}
    for fuser in filtered_users:
        if fuser.profile.genero not in genero:
            genero[fuser.profile.genero] = 1
        else:
            genero[fuser.profile.genero] += 1

    labels = list(genero.keys())
    n_pessoas = list(genero.values())
    labels_with_count = ['{} ({})'.format(label, count) for label, count in zip(labels, n_pessoas)]

    plt.figure(figsize=(8, 6))
    plt.pie(n_pessoas, labels=labels_with_count, autopct='%.2f%%', counterclock=False, startangle=90, colors=cores)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_genero = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return grafico_genero

def cria_grafico_tipo_usuario(filtered_users):
    # Grafico usuarios por tipo de usuário
    tipo_usuario = {}
    for fuser in filtered_users:
        if fuser.profile.tipo_usuario not in tipo_usuario:
            tipo_usuario[fuser.profile.tipo_usuario] = 1
        else:
            tipo_usuario[fuser.profile.tipo_usuario] += 1

    labels = list(tipo_usuario.keys())
    n_pessoas = list(tipo_usuario.values())
    labels_with_count = ['{} ({})'.format(label, count) for label, count in zip(labels, n_pessoas)]

    plt.figure(figsize=(8, 6))
    plt.pie(n_pessoas, labels=labels_with_count, autopct='%.2f%%', counterclock=False, startangle=90, colors=cores)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_tipo_usuario = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return grafico_tipo_usuario

def cria_grafico_faculdade(filtered_users):
    # Grafico usuarios por faculdade
    faculdade = {}
    for fuser in filtered_users:
        if fuser.profile.faculdade not in faculdade:
            faculdade[fuser.profile.faculdade] = 1
        else:
            faculdade[fuser.profile.faculdade] += 1

    labels = list(faculdade.keys())
    n_pessoas = list(faculdade.values())
    labels_with_count = ['{} ({})'.format(label, count) for label, count in zip(labels, n_pessoas)]

    plt.figure(figsize=(8, 6))
    plt.pie(n_pessoas, labels=labels_with_count, autopct='%.2f%%', counterclock=False, startangle=90, colors=cores)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_faculdade = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return grafico_faculdade

def cria_grafico_renda(filtered_users):
    # Grafico usuarios por renda
    renda = {}
    for fuser in filtered_users:
        if fuser.profile.renda_familiar not in renda:
            renda[fuser.profile.renda_familiar] = 1
        else:
            renda[fuser.profile.renda_familiar] += 1

    labels = list(renda.keys())
    n_pessoas = list(renda.values())
    labels_with_count = ['{} ({})'.format(label, count) for label, count in zip(labels, n_pessoas)]

    plt.figure(figsize=(8, 6))
    plt.pie(n_pessoas, labels=labels_with_count, autopct='%.2f%%', counterclock=False, startangle=90, colors=cores)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_renda = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return grafico_renda

def cria_grafico_estado_nascimento(filtered_users):
    # Grafico usuarios por estado de nascimento
    estado_nascimento = {}
    for fuser in filtered_users:
        if fuser.profile.estado_nascimento not in estado_nascimento:
            estado_nascimento[fuser.profile.estado_nascimento] = 1
        else:
            estado_nascimento[fuser.profile.estado_nascimento] += 1

    labels = list(estado_nascimento.keys())
    n_pessoas = list(estado_nascimento.values())
    labels_with_count = ['{} ({})'.format(label, count) for label, count in zip(labels, n_pessoas)]

    plt.figure(figsize=(8, 6))
    plt.pie(n_pessoas, labels=labels_with_count, autopct='%.2f%%', counterclock=False, startangle=90, colors=cores)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_estado_nascimento = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return grafico_estado_nascimento

def cria_grafico_pais_atual(filtered_users):
    # Grafico usuarios por país atual
    pais_atual = {}
    for fuser in filtered_users:
        if fuser.profile.pais_atual not in pais_atual:
            pais_atual[fuser.profile.pais_atual] = 1
        else:
            pais_atual[fuser.profile.pais_atual] += 1

    labels = list(pais_atual.keys())
    n_pessoas = list(pais_atual.values())
    labels_with_count = ['{} ({})'.format(label, count) for label, count in zip(labels, n_pessoas)]

    plt.figure(figsize=(8, 6))
    plt.pie(n_pessoas, labels=labels_with_count, autopct='%.2f%%', counterclock=False, startangle=90, colors=cores)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_pais_atual = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return grafico_pais_atual

def cria_grafico_estado_atual(filtered_users):
    # Grafico usuarios por estado atual
    estado_atual = {}
    for fuser in filtered_users:
        if fuser.profile.estado_atual != None:
            if fuser.profile.estado_atual not in estado_atual:
                estado_atual[fuser.profile.estado_atual] = 1
            else:
                estado_atual[fuser.profile.estado_atual] += 1

    labels = list(estado_atual.keys())
    n_pessoas = list(estado_atual.values())
    labels_with_count = ['{} ({})'.format(label, count) for label, count in zip(labels, n_pessoas)]

    plt.figure(figsize=(8, 6))
    plt.pie(n_pessoas, labels=labels_with_count, autopct='%.2f%%', counterclock=False, startangle=90, colors=cores)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_estado_atual = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return grafico_estado_atual
