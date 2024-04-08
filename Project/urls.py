"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('login/', user_views.login, name='app-login'),
    path('register/', user_views.register, name='app-register'),
    path('logout/', user_views.logout, name='app-logout'),
    path('profile/', user_views.profile, name='app-profile'),
    path('profile/edit/', user_views.edit, name='app-edit'),
    path('profile/change_password/', user_views.change_password, name='app-passwd'),
    path('profile/delete/', user_views.delete, name='app-delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
