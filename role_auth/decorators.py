from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'ADMIN':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

def agent_required(view_func):
    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'AGENT':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper
# Custom decorators for the accounts app