"""garda_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('pages.urls'), name='index'),
    path('users/', include('models.urls')), 
    #path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    
    # allauth url
    path('accounts/', include('allauth.urls')),


    #re_path(r'^accounts/', include('allauth.urls')),
    #path('accounts/', TemplateView.as_view(template_name='accounts/index.html')),
    #path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'))
]
