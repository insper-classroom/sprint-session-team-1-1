from django.shortcuts import render

# Create your views here.
# Mostra a home page:
def home(request):
    return render(request, 'home-page/home.html')

# Eu testando:
def login(request):
    return render(request, 'templates/account/login.html')