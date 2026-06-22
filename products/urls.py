from django.urls import path, include

from products.views.main import home_view
from products.views.auth import login_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('register/', lambda r: __import__('django.shortcuts', fromlist=['redirect']).redirect('/accounts/signup/'),
         name='register'),

    path('accounts/', include('allauth.urls')),  # Google OAuth

]