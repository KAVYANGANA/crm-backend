from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        AGENT = 'AGENT', 'Agent'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.AGENT
    )

# Create your models here.
