from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'status', 'assigned_to', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('status',)