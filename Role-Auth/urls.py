from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('agent-dashboard/', views.agent_dashboard, name='agent_dashboard'),
    path('agents/', views.agent_list, name='agent_list'),
    path('agents/<int:agent_id>/', views.agent_detail, name='agent_detail'),
    path('agents/<int:agent_id>/edit/', views.agent_edit, name='agent_edit'),
    path('agent-profile/', views.agent_profile, name='agent_profile'),
    path('admin-signup/', views.admin_signup, name='admin_signup'),

    # Add your URL patterns here
]