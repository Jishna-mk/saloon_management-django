from django.urls import path
from .import views

urlpatterns = [
    path('customer_signup/',views.customer_signup,name='customer_signup'),
    path('shop_owner_signup/',views.shop_owner_signup,name='shop_owner_signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.login_user,name='logout'),
    path('customer_profile/',views.create_customer_profile,name='customer_profile'),
    path('view_profile/',views.view_customer_profile,name='view_profile'),
    path('view_staff/',views.view_staff,name='view_staff'),
    
]