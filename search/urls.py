from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.profile_id, name='profile_id'),
    path('', views.individual_table, name='individual_table'),
]