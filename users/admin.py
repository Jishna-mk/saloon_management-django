from django.contrib import admin
from .models import User,CustomerProfile
# Register your models here.

admin.site.register(User),
admin.site.register(CustomerProfile)