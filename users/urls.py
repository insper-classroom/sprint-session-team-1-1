from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/historico/', views.historico, name='historico'),
    path('profile/edit/', views.edit, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
]