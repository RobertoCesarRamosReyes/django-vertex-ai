"""
URL configuration for rcrr_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from first_app.views import my_view
from second_app.views import my_view2
from vertex_ai_app.views import generate_content_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test',my_view),
    path('test2',my_view2),
    path('vertex',generate_content_view)
]
