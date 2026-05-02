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
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    company_image = models.ImageField(upload_to='company_images/', blank=True, null=True)

    def __str__(self):
        return self.username
# Create your models here.
