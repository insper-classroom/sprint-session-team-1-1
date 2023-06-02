from django.contrib.auth.admin import UserAdmin # UserAdmin é a classe de administração padrão para o modelo de usuário do Django
from .models import User, Profile
from django.contrib import admin

class ProfileInline(admin.StackedInline): # admin.StackedInline é uma classe que permite que o Profile seja editado na mesma página do User e que define como um modelo é exibido como um conjunto empilhado de campos em um formulário.
    model = Profile
    can_delete = False # Impede que os objetos 'Profile' sejam excluídos em linha junto com o objeto 'User' na página de administração.
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,) # faz com que o formulário 'Profile' seja exibido na página de administração do User

admin.site.unregister(User) # Desregistra o UserAdmin padrão 
admin.site.register(User, CustomUserAdmin) # Registra o CustomUserAdmin como o novo UserAdmin 
