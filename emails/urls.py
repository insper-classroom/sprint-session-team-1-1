from django.urls import path, include # include is new
from users.views import custom_logout
from . import views

urlpatterns = [
    path('email/', views.test, name="test"),
]
