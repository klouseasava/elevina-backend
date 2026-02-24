"""
URL configuration for elevina_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include  # include is needed for app urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/accounts/', include('accounts.api.urls')),
    path('api/contributions/', include('contribution.api.urls')),
    path('api/allocations/', include('allocation.api.urls')),
    path('api/vouchers/', include('vouchers.api.urls')),
    path('api/treasury/', include('treasury.api.urls')),
]
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT AUTH
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Your APIs
    path('api/accounts/', include('accounts.api.urls')),
    path('api/contribution/', include('contribution.api.urls')),
    path('api/allocation/', include('allocation.api.urls')),
    path('api/vouchers/', include('vouchers.api.urls')),
    path('api/treasury/', include('treasury.api.urls')),
]
