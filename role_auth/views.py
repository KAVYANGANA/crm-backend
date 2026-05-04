from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .decorators import admin_required, agent_required
from django.shortcuts import get_object_or_404

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.role == 'ADMIN':
                return redirect('admin_dashboard')
            elif user.role == 'AGENT':
                return redirect('agent_dashboard')

        messages.error(request, 'Invalid username or password')
        return redirect('login')

    return render(request, 'accounts/login.html')
def admin_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        company_name = request.POST.get("company_name")
        company_email = request.POST.get("company_email")
        company_image = request.FILES.get("company_image")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role="ADMIN",
            company_name=company_name,
            company_email=company_email,
            company_image=company_image
        )

        messages.success(request, "Admin registered successfully")
        return redirect("login")

    return render(request, "accounts/admin_signup.html")


def logout_view(request):
    logout(request)
    return redirect('login')
@admin_required
def admin_dashboard(request):
    admin_user = request.user
    return render(request, 'accounts/admin_dashboard.html', {'admin': admin_user})
@agent_required
def agent_dashboard(request):
    return render(request, 'accounts/agent_dashboard.html')
@admin_required
def agent_list(request):
    agents = User.objects.filter(role='AGENT')
    return render(request, 'accounts/agent_list.html', {'agents': agents})
@admin_required
def agent_detail(request, agent_id):
    agent = get_object_or_404(User, id=agent_id, role='AGENT')
    return render(request, 'accounts/agent_detail.html', {'agent': agent})
@admin_required
def agent_edit(request, agent_id):
    agent = get_object_or_404(User, id=agent_id, role='AGENT')

    if request.method == 'POST':
        agent.username = request.POST.get('username')
        agent.email = request.POST.get('email')
        agent.save()
        return redirect('agent_detail', agent_id=agent.id)

    return render(request, 'accounts/agent_edit.html', {'agent': agent})
@agent_required
def agent_profile(request):
    return render(request, 'accounts/agent_profile.html', {'agent': request.user})


# Create your views here.

