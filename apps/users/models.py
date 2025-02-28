from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('tenant', 'Tenant'),
        ('owner', 'Owner'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()

class HouseOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner")
    verification_status = models.BooleanField(default=False)
