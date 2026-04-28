from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Agent
from .serializers import AgentSerializer


class AgentViewSet(ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
