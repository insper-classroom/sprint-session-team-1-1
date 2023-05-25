from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='perfil'),
    path('', views.signup, name='signup'),
]