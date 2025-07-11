"""
URL configuration for weblog project.

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
from posts.urls import urlpatterns
from django.urls import path, include
from posts.views import post_list, post_detail
from posts.api.api import AllWeblogs, DetailWeblog, CreateComment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weblog/', include('posts.urls', namespace='posts')),
]