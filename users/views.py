from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User,CustomerProfile
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerProfileForm

# Create your views here.

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email', 'password1', 'password2']


def customer_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.save()
            return redirect('login')
    return render(request,'users/customer_signup.html')


def shop_owner_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_shop_owner = True
            var.save()
            return redirect('login')
    return render(request,'users/shop_owner_signup.html')


def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request,'You Are Successfully Logged In!!')
            return redirect('viewpage')
        else:
            messages.warning(request,'Something Went Wrong!!')
            return redirect('login')
    return render(request,'users/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'You Are Logged Out!!')
    return redirect('login')


from .forms import CustomerProfileForm  

from django.shortcuts import redirect
from django.http import HttpResponseBadRequest

def create_customer_profile(request):
    # Check if the user already has a profile
    if hasattr(request.user, 'customer_profile'):
        # Redirect to view the existing profile
        return redirect('view_profile')
    
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('view_profile') 
    else:
        form = CustomerProfileForm()
    return render(request, 'users/create_customer_profile.html', {'form': form})




from django.contrib.auth.models import User

def view_customer_profile(request):
    try:
        customer_profile = request.user.customer_profile
    except CustomerProfile.DoesNotExist:
        customer_profile = None

    return render(request, 'users/view_customer_profile.html', {'customer_profile': customer_profile, 'user': request.user})
from packages.models import staffProfile

def view_staff(request):
    profiles = staffProfile.objects.all()
    return render(request, 'users/view_staff.html', {'profiles': profiles})