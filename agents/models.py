from django.db import models
from django.conf import settings


class Agent(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
