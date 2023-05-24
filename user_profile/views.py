from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

@login_required
def profile(request):
    return HttpResponse('<h1>Profile</h1>')

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('<h1>Usuário editado com sucesso!</h1>')
    else:
        user_form = UserProfileForm(instance=request.user)
        return render(request, 'user_profile/user_profile-edit.html', {'user_form': user_form})
