from django.urls import path
from . import views
from user_profile import views as vw
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', vw.edit, name='edit_profile'),
]