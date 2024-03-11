from django.urls import path
from .import views

urlpatterns = [
    path('add_packages/',views.add_package,name='add_packages'),
    path('update_package/<int:package_id>/',views.update_package,name='update_package'),
    path('packages_list/',views.packages_list,name='packages_list'),
    path('package_details/<int:package_id>/',views.package_detail,name='package_details'),
    path('apply-to-package/<int:pk>/',views.apply_to_package,name='apply-to-package'),
    path('applied_package/',views.applied_packages,name='applied_package'),
    path('manage_package/',views.manage_package,name='manage_package'),
    path('delete_package/<int:pk>/',views.delete_package,name='delete_package'),
    path('all_applicants/<int:pk>/',views.all_applicants,name='all_applicants'),
    path('approve_application/<int:applicant_id>/',views.approve_application,name='approve_application'),
    path('decline_application/<int:applicant_id>/',views.decline_application,name='decline_application'),
    path('add_staff_profile/', views.add_staff_profile, name='add_staff_profile'),
    path('view_staff_profiles/', views.view_staff_profiles, name='view_staff_profiles'),
    path('delete_staff_profile/<int:profile_id>/', views.delete_staff_profile, name='delete_staff_profile'),
    path('admin_signin/',views.admin_signin,name="admin_signin"),
    path('admin_signout/',views.admin_signout,name="admin_signout"),
    path('dashboard/',views.dashboard,name="dashboard")

    
]