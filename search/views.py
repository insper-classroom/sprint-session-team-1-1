from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def individual_table(request):
    user = request.user
    profile = user.profile 
    if profile.tipo_usuario != 'Colaborador' and profile.tipo_usuario != 'Admin':
        return redirect('/')
    else:
        return redirect('/accounts/profile/')