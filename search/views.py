from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.
@login_required
def individual_table(request):
    user = request.user
    profile = user.profile 
    if profile.tipo_usuario != 'Colaborador' and profile.tipo_usuario != 'Admin':
        return redirect('/')
    else:
        all_users = User.objects.all().order_by('-date_joined')
        return render(request, 'search/search.html', {'users': all_users})