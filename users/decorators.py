from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):  # define se um usuario está autenticado
    def wrapper_func(request, *arg, **kwargs):
        if request.user.is_authenticated:
            return redirect ('')
        else:
            return view_func(request, *arg, **kwargs)
        
    return wrapper_func
    
def allowed_users(allowed_roles=[]):  # define os grupos permitidos para acessar as views
    def decorator(view_func):
        def wrapper_func(request, *arg, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *arg, **kwargs)
            else:
                return HttpResponse('voce nao esta autroizado para ver esta view')
        return wrapper_func
    return decorator