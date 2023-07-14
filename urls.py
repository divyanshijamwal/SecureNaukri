"""securenaukri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from securenaukri import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('companies/',views.companies, name='companies'),
    path('job_detail/',views.job_detail, name='detail'),
    path('job_detail/<int:post>',views.jobpost, name='post'),
    path('contact/',views.contact, name='contact'),
    path('privacy/',views.privacy, name='privacy'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('jobpostingrules/',views.jobpostingrules, name='rules'),
    path('explore/', views.explore, name='explore'),
    path('employer/', views.employer, name='employer'),
    path('reset/', views.reset, name='reset'),
    path('manage/', views.manage, name='manage'),
]










