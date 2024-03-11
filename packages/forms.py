from django import forms
from .models import Package
from .models import staffProfile

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'price', 'duration', 'image', 'is_available', 'discount_percentage', 'category']


class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = staffProfile
        fields = ['username','phone_number', 'location','photo']

    def __init__(self, *args, **kwargs):
        super(StaffProfileForm, self).__init__(*args, **kwargs)

