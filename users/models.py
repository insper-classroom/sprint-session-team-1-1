from django.db import models
from django.contrib.auth.models import AbstractUser # AbstractUser é a classe de usuários padrão do Django e adicionamos mais campos/dados a ela

# Create your models here.
class CustomUser(AbstractUser): # classe de usuários customizada
    
    STATUS = (
        ('regular', 'regular'), # É o Usuário - qualquer usuário do sistema
        ('bolsista', 'bolsista'),
        ('colaborador', 'colaborador'),
        ('administrador', 'administrador'),
        ('sponsor', 'sponsor'), # Quem paga o projeto vê tudo de forma mais generalizada
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular') # O default é qualquer usuário do sistema (regular)
    # Acho que aqui deve-se colocar os novos campos

    def __str__(self):
        return self.email # Adotei que retorna email como string de usuário, mas pode ser qualquer outro campo
    