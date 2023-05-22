from django.db import models
from django.contrib.auth.models import User # User é a classe de usuário padrão do Django que já vem com um pacote de autenticação.


# Create your models here.
class Profile(models.Model): # Profile é uma classe que adiciona mais campos/dados ao User do Django, para os usuários bolsistas
    
    Genders = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Prefiro não informar', 'Prefiro não informar'),
        ('Outro', 'Outro'),
    )

    Race = (
        ('Amarela', 'Amarela'),
        ('Branca', 'Branca'),
        ('Indígena', 'Indígena'),
        ('Parda', 'Parda'),
        ('Preta', 'Preta'),
        ('Prefiro não informar', 'Prefiro não informar'),
        ('Outra', 'Outra'),
    )

    nome_completo = models.CharField(max_length=150, null=True, verbose_name='Nome Completo') # null=True porque quando o usuário se registrar, cria-se automaticamente um objeto do tipo perfil ligado à esse usuário que ainda não preencheu o nome completo. Por isso, inicialmente, no banco de dados, o valor é nulo.
    email = models.EmailField(max_length=254, null=True, verbose_name='E-mail') # EmailField é um campo de email, que não pode ser maior que 254 caracteres
    nome_exibicao = models.CharField(max_length=50, null=True, verbose_name='Nome de exibição') # Nome que será exibido no site, se não for preenchido, será o nome completo
    # foto_de_perfil = ...
    data_nascimento = models.DateField(null=True, verbose_name='Data de nascimento') # dd/mm/aaaa (vamos usar uma máscara, para as /)
    cpf = models.CharField(max_length=14, null=True, verbose_name='CPF') # xxx.xxx.xxx-xx (vamos usar uma máscara, para os . e -)
    rg = models.CharField(max_length=12, null=True, verbose_name='RG') # xx.xxx.xxx-x (vamos usar uma máscara, para os . e -)
    telefone = models.CharField(max_length=15, null=True) # (xx) xxxxx-xxxx (vamos usar uma máscara, para os () e -)
    genero = models.CharField(max_length=20, choices=Genders, null=True, verbose_name='Gênero') # choices é uma tupla de tuplas, onde o primeiro elemento de cada tupla é o valor que será salvo no banco de dados e o segundo é o valor que será exibido no site (verbose_name é o nome que será exibido no site
    outro_genero = models.CharField(max_length=100, blank=True, null=True, verbose_name='Outro') # Se o usuário escolher "Outro", ele pode escrever o que quiser aqui
    cor_ou_raca = models.CharField(max_length=20, choices=Race, null=True, verbose_name='Cor ou Raça')
    outra_cor_ou_raca = models.CharField(max_length=100, blank=True, null=True, verbose_name='Outra')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) # Um usuário tem UM perfil, e quando o usuário é deletado, o perfil também é (CASCADE).