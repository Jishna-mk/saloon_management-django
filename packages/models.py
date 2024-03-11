# models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Package(models.Model):
    category_type_choices = [
        ('Haircare', 'Haircare'),
        ('Skincare', 'Skincare'),
        ('Spa', 'Spa')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='package_images/', blank=True, null=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    category = models.CharField(max_length=20, choices=category_type_choices, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    shop_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='packages')

    def __str__(self):
        return self.name


class ApplyPackage(models.Model):
    status_choices = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applied_packages')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='applications')
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')

    def __str__(self):
        return f"{self.user.username} applied for {self.package.name} ({self.status})"
    

class staffProfile(models.Model):
    username=models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='package_images/', null=True, blank=True)

      