"""
URL configuration for bazar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework_simplejwt import views as jwt_views

import background_field

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/users/", include("user.urls")),
    path("api/v1/products/", include("product.urls")),
    path("api/v1/wholesales/", include("whole_sale.urls")),
    path("api/v1/services/", include("service.urls")),
    path("api/v1/background_field/", include("background_field.urls")),
]
