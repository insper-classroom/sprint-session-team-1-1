from django.db import models
from django.contrib.auth.models import User # User é a classe de usuário padrão do Django que já vem com um pacote de autenticação.

# Create your models here.
class Profile(models.Model): # Profile é uma classe que adiciona mais campos/dados ao User do Django, para os usuários bolsistas
    nome_completo = models.CharField(max_length=100, null=True) # null=True porque quando o usuário se registrar, cria-se automaticamente um objeto do tipo perfil ligado à esse usuário que ainda não preencheu o nome completo. Por isso, inicialmente, no banco de dados, o valor é nulo.
    cpf = models.CharField(max_length=14, null=True) # xxx.xxx.xxx-xx (vamos usar uma máscara, para os . e -)
    telefone = models.CharField(max_length=15, null=True) # (xx) xxxxx-xxxx (vamos usar uma máscara, para os () e -)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) # Um usuário tem UM perfil, e quando o usuário é deletado, o perfil também é (CASCADE).