from django.urls import path
from . import views

urlpatterns = [
    path('history/professional/<int:user_id>', views.history_id_professional, name='profile_id'),
    path('history/academic/<int:user_id>', views.history_id_academic, name='profile_id'),
    path('<int:user_id>', views.profile_id, name='profile_id'),
    path('overview/', views.charts, name='graficos'),
    path('', views.individual_table, name='individual_table'),
]