from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Lead
from .serializers import LeadSerializer


class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin users (safe default)
        if user.is_staff:
            return Lead.objects.all()

        # Normal users see only assigned leads
        return Lead.objects.filter(assigned_to=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)