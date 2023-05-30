from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users import models

@login_required
def profile(request):
    return HttpResponse('<h1>Profile</h1>')

@login_required
def edit(request):
    user_id = request.user.id
    if request.method == 'POST':
        user_form = models.Profile.objects.get(id=user_id)  # Supondo que o Profile tenha um campo 'user' referenciando o objeto User
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('<h1>Usuário editado com sucesso!</h1>')
    else:
        user_form = models.Profile.objects.get(id=user_id)
        return render(request, 'user_profile/user_profile-edit.html', {'user_form': user_form})
