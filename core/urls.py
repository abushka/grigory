"""grigory URL Configuration

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
from django.urls import path, include

from core.settings import REST_EXPOSE_AUTH_API, DJANGO_BASE_PATH, EXPOSE_DEMO_SITE

urlpatterns = [
    path(DJANGO_BASE_PATH + 'admin/', admin.site.urls),
]

if REST_EXPOSE_AUTH_API:
    urlpatterns += [
        path(DJANGO_BASE_PATH + 'api/auth/', include('authentication.api.urls'), name='authentication'),
    ]

urlpatterns += [
    path(DJANGO_BASE_PATH + 'api/', include('app.api.urls'))
]

if EXPOSE_DEMO_SITE:
    urlpatterns += [
        path(DJANGO_BASE_PATH + '', include('demo.urls'))
    ]
