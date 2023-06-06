from django.urls import path, include # include is new
from users.views import custom_logout
from users.views import generate_link
from django.contrib import admin

from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', include('allauth.urls')),
    path('accounts/logout/', custom_logout, name='logout'),
    path('accounts/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('search/', include('search.urls')),
    path('generate/', generate_link, name='generate'),
    path('', views.home, name='home'),
]
