# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_shop_owner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='package_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"