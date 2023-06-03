from django.urls import path
from . import views

urlpatterns = [
    path('', views.individual_table, name='individual_table'),
]