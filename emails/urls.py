from django.urls import path, include # include is new
from users.views import custom_logout
from . import views

urlpatterns = [
    path('done/', views.test, name="test"),
    path('sendemail/', views.send_email_to_all, name="sendemail"),
    path('emailperiodic/', views.send_email_particular_time, name="emailperiodic"),
]
