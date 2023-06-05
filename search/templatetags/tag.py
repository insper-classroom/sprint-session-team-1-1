from django import template
from datetime import datetime

register = template.Library()

# Cria a tag que sera usada para gerar o path da imagem do usuario
@register.simple_tag
def image_path(image):
    path_image = "/".join(str(image).split('/')[2:])
    return path_image

@register.simple_tag
def age(nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual-nascimento
    return idade
