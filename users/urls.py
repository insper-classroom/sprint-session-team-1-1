from django.urls import path
from . import views


urlpatterns = [
    path('signup/<str:key>', views.signup, name='signup'),
    path('signup/', views.redirect_home, name='redirect_home'), # redirect_home é uma função que redireciona para a página inicial
    path('profile/history/academic', views.historico_academico, name='historico_escolar'),
    path('profile/history/professional', views.historico_profissional, name='historico_profissional'),
    path('profile/edit/', views.edit, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
]