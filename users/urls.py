from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/historico/escolar', views.historico_escolar, name='historico'),
    path('profile/historico/profissional', views.historico_profissional, name='historico_profissional'),
    path('profile/edit/', views.edit, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
]