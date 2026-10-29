"""
URL configuration for locallibrary_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Use include() to add paths from the catalog application
from django.urls import include, path

# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

from taskflow.api import api as taskflow_api
from taskflow.api import api_v2 as taskflow_api_v2

# locallibrary_config/urls.py
# (after the existing blocks)
# Mount the Django Ninja API
from .api import api

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path("catalog/", include("catalog.urls")),
    path("chat/", include("chat.urls")),
]

urlpatterns += [
    path("", RedirectView.as_view(url="catalog/")),
]

# Add django-allauth's account urls (for login, logout, sign-up, password management)
urlpatterns += [
    path("accounts/", include("allauth.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("api/", api.urls),
]

urlpatterns += [
    path("taskflow/api/v2/", taskflow_api_v2.urls),
    path("taskflow/api/", taskflow_api.urls),
]
