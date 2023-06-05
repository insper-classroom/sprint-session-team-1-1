from django.db.models import Q
from datetime import datetime


def apply_filters(users, request):
    busca_nome = request.GET.get('busca-nome')
    busca_sobrenome = request.GET.get('busca-sobrenome')
    busca_exibicao = request.GET.get('busca-exibicao')
    cor_amarela = request.GET.get('cor-amarela')
    cor_branca = request.GET.get('cor-branca')
    cor_indigena = request.GET.get('cor-indigena')
    cor_parda = request.GET.get('cor-parda')
    cor_preta = request.GET.get('cor-preta')
    cor_nao = request.GET.get('cor-nao')
    cor_outra = request.GET.get('cor-outra')
    genero_masculino = request.GET.get('genero-masculino')
    genero_feminino = request.GET.get('genero-feminino')
    genero_nao = request.GET.get('genero-nao')
    genero_outro = request.GET.get('genero-outro')
    usuario_bolsista = request.GET.get('usuario-bolsista')
    usuario_alumni = request.GET.get('usuario-alumni')
    faculdade_insper = request.GET.get('faculdade-insper')
    faculdade_inteli = request.GET.get('faculdade-inteli')
    faculdade_facul3 = request.GET.get('faculdade-facul3')
    renda_01 = request.GET.get('renda-01')
    renda_12 = request.GET.get('renda-12')
    renda_23 = request.GET.get('renda-23')
    renda_35 = request.GET.get('renda-35')
    renda_58 = request.GET.get('renda-58')
    renda_8 = request.GET.get('renda-8')
    busca_id = request.GET.get('filtro-id')
    busca_cpf = request.GET.get('filtro-cpf')
    busca_rg = request.GET.get('filtro-rg')
    busca_email = request.GET.get('filtro-email')
    busca_numero = request.GET.get('filtro-numero')
    busca_curso = request.GET.get('filtro-curso')
    busca_estado_nascimento = request.GET.get('filtro-estado-nascimento')
    busca_estado_atual = request.GET.get('filtro-estado-atual')
    busca_cidade_nascimento = request.GET.get('filtro-cidade-nascimento')
    busca_cidade_atual = request.GET.get('filtro-cidade-atual')
    busca_pais_atual = request.GET.get('filtro-pais-atual')
    busca_ano_nascimento = request.GET.get('filtro-ano-nascimento')
    busca_ano_matricula = request.GET.get('filtro-ano-matricula')
    busca_ano_formatura = request.GET.get('filtro-ano-formatura')
    busca_ano_inicial = request.GET.get('filtro-ano-inicial')
    busca_ano_final = request.GET.get('filtro-ano-final')

    filters = Q()

    if busca_nome:
        filters &= Q(profile__nome__icontains=busca_nome)

    if busca_sobrenome:
        filters &= Q(profile__sobrenome__icontains=busca_sobrenome)

    if busca_exibicao:
        filters &= Q(profile__nome_exibicao__icontains=busca_exibicao)

    if busca_id:
        filters &= Q(id=busca_id)

    if busca_cpf:
        filters &= Q(profile__cpf__icontains=busca_cpf)

    if busca_rg:
        filters &= Q(profile__rg__icontains=busca_rg)

    if busca_email:
        filters &= Q(email__icontains=busca_email)

    if busca_numero:
        filters &= Q(profile__telefone__icontains=busca_numero)

    if busca_curso:
        filters &= Q(profile__curso__icontains=busca_curso)

    if busca_estado_nascimento:
        filters &= Q(profile__estado_nascimento__icontains=busca_estado_nascimento)

    if busca_estado_atual:
        filters &= Q(profile__estado_atual__icontains=busca_estado_atual)

    if busca_cidade_nascimento:
        filters &= Q(profile__cidade_nascimento__icontains=busca_cidade_nascimento)

    if busca_cidade_atual:
        filters &= Q(profile__cidade_atual__icontains=busca_cidade_atual)

    if busca_pais_atual:
        filters &= Q(profile__pais_atual__icontains=busca_pais_atual)

    if busca_ano_nascimento:
        year = int(busca_ano_nascimento)
        filters &= Q(profile__data_nascimento__year=year)

    if busca_ano_matricula:
        year_matricula = int(busca_ano_matricula)
        filters &= Q(profile__ano_ingresso=year_matricula)

    if busca_ano_formatura:
        year_formatura = int(busca_ano_formatura)
        filters &= Q(profile__ano_formatura=year_formatura)

    if busca_ano_inicial and busca_ano_final:
        initial_year = int(busca_ano_inicial)
        final_year = int(busca_ano_final)
        filters &= Q(profile__data_nascimento__year__range=(initial_year, final_year))



    if cor_amarela or cor_branca or cor_indigena or cor_parda or cor_preta or cor_nao or cor_outra:
        cor_filters = Q()
        if cor_amarela:
            cor_filters |= Q(profile__cor_ou_raca='Amarela')
        if cor_branca:
            cor_filters |= Q(profile__cor_ou_raca='Branca')
        if cor_indigena:
            cor_filters |= Q(profile__cor_ou_raca='Indígena')
        if cor_parda:
            cor_filters |= Q(profile__cor_ou_raca='Parda')
        if cor_preta:
            cor_filters |= Q(profile__cor_ou_raca='Preta')
        if cor_nao:
            cor_filters |= Q(profile__cor_ou_raca='Prefiro Não Informar')
        if cor_outra:
            cor_filters |= Q(profile__cor_ou_raca='Outra')
        filters &= cor_filters

    if genero_masculino or genero_feminino or genero_nao or genero_outro:
        genero_filters = Q()
        if genero_masculino:
            genero_filters |= Q(profile__genero='Masculino')
        if genero_feminino:
            genero_filters |= Q(profile__genero='Feminino')
        if genero_nao:
            genero_filters |= Q(profile__genero='Prefiro Não Informar')
        if genero_outro:
            genero_filters |= Q(profile__genero='Outro')
        filters &= genero_filters

    if usuario_bolsista or usuario_alumni:
        usuario_filters = Q()
        if usuario_bolsista:
            usuario_filters |= Q(profile__tipo_usuario='Bolsista')
        if usuario_alumni:
            usuario_filters |= Q(profile__tipo_usuario='Alumni')
        filters &= usuario_filters

    if faculdade_insper or faculdade_inteli or faculdade_facul3:
        faculdade_filters = Q()
        if faculdade_insper:
            faculdade_filters |= Q(profile__faculdade='Insper')
        if faculdade_inteli:
            faculdade_filters |= Q(profile__faculdade='Inteli')
        if faculdade_facul3:
            faculdade_filters |= Q(profile__faculdade='Facul3')
        filters &= faculdade_filters

    if renda_01 or renda_12 or renda_23 or renda_35 or renda_58 or renda_8:
        renda_filters = Q()
        if renda_01:
            renda_filters |= Q(profile__renda_familiar__lte=1)
        if renda_12:
            renda_filters |= Q(profile__renda_familiar__range=(1, 2))
        if renda_23:
            renda_filters |= Q(profile__renda_familiar__range=(2, 3))
        if renda_35:
            renda_filters |= Q(profile__renda_familiar__range=(3, 5))
        if renda_58:
            renda_filters |= Q(profile__renda_familiar__range=(5, 8))
        if renda_8:
            renda_filters |= Q(profile__renda_familiar__gte=8)
        filters &= renda_filters

    return users.filter(filters)
