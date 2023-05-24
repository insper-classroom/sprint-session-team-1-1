from django.urls import path, include
from . import views

urlpatterns = [     
    path('edit/', views.edit, name='edit'),
    path('', views.profile, name='profile')
]