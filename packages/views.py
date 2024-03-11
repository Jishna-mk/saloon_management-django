from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Package,ApplyPackage
from .forms import PackageForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def admin_signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("dashboard")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("admin_signin")

    return render(request,"admin/admin_signin.html")


def admin_signout(request):
    logout(request)
    return redirect("admin_signin")  


from django.contrib.auth.models import User
from users.models import CustomerProfile

def dashboard(request):
 
    staff_count = staffProfile.objects.count()

    customer_count = CustomerProfile.objects.count()

    staff_profiles = staffProfile.objects.all()

   
    customer_profiles = CustomerProfile.objects.all()

    return render(request, "admin/dashboard.html", {
        'staff_count': staff_count,
        'customer_count': customer_count,
        'staff_profiles': staff_profiles,
        'customer_profiles': customer_profiles,
    })

@login_required
def add_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save(commit=False)
            package.shop_owner = request.user
            package.save()
            return redirect('packages_list')
    else:
        form = PackageForm()

        return render(request, 'packages/add_package.html', {'form': form})
   
    return render(request, 'website/viewpage.html')


@login_required
def update_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    if package.shop_owner != request.user:
        
        messages.info(request,"You are not authorized to update this package")

    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            return redirect('packages_list')
    else:
        form = PackageForm(instance=package)

    return render(request, 'packages/update_package.html', {'form': form, 'package': package})


# def update_package(request, package_id):
#     package = get_object_or_404(Package, id=package_id, shop_owner=request.user)

#     if request.method == 'POST':
#         form = PackageForm(request.POST, request.FILES, instance=package)
#         if form.is_valid():
#             form.save()
#             return redirect('packages_list')
#     else:
#         form = PackageForm(instance=package)

#     return render(request, 'packages/update_package.html', {'form': form, 'package': package})



def packages_list(request):
    packages = Package.objects.all()
    return render(request, 'packages/packages_list.html', {'packages': packages})


def package_detail(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    
    
    has_applied = False
    if request.user.is_authenticated and request.user.is_customer:
        has_applied = ApplyPackage.objects.filter(user=request.user, package=package).exists()

    return render(request, 'packages/package_detail.html', {'package': package, 'has_applied': has_applied})



def apply_to_package(request, pk):
    if request.user.is_authenticated and request.user.is_customer:
        package = get_object_or_404(Package, pk=pk)

        
        if ApplyPackage.objects.filter(user=request.user, package=package).count() > 0:
            messages.warning(request, 'Permission Denied')
            return redirect('viewpage')
        else:
            ApplyPackage.objects.create(
                package=package,
                user=request.user,
                status='Pending'  
            )
            messages.info(request, 'You have successfully applied!!')
            return redirect('viewpage')
    else:
        messages.warning(request, 'Sorry, you must be logged in to view that page!!')
        return redirect('login')
    

def applied_packages(request):
    packages = ApplyPackage.objects.filter(user=request.user)
    context = {"packages" : packages}
    return render(request, 'users/applied_packages.html',context)


def manage_package(request):
    packages = Package.objects.filter(shop_owner=request.user)
    context = {"packages": packages}
    return render(request, 'packages/manage_packages.html', context)


def delete_package(request, pk):
    if request.user.is_authenticated and request.user.is_shop_owner:
        package =Package.objects.get(pk=pk)
        package.delete()
        return redirect('manage_package') 
    else:
        return render(request, 'packages/manage_packages.html')


def all_applicants(request,pk):
    package = Package.objects.get(pk=pk)
    applicants = package.applications.exclude(status='Accepted')
    context = {"package":package, "applicants":applicants}
    return render(request, 'packages/all_applicants.html',context)


def approve_application(request, applicant_id):
    application = get_object_or_404(ApplyPackage, id=applicant_id)
    application.status = 'Accepted'
    application.save()
    return redirect('manage_package')

def decline_application(request, applicant_id):
    application = get_object_or_404(ApplyPackage, id=applicant_id)
    application.status = 'Declined'
    application.save()
    return redirect('manage_package')


# views.py

from .forms import StaffProfileForm
from .models import staffProfile
from django.shortcuts import render, redirect

# views.py

def add_staff_profile(request):
    if request.method == 'POST':
        form = StaffProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_staff_profiles')
    else:
        form = StaffProfileForm()
    return render(request, 'packages/add_staff_profile.html', {'form': form})

def view_staff_profiles(request):
    profiles = staffProfile.objects.all()
    return render(request, 'packages/view_staff_profile.html', {'profiles': profiles})

def delete_staff_profile(request, profile_id):
    profile = get_object_or_404(staffProfile, id=profile_id)
    profile.delete()
    return redirect('view_staff_profiles')

