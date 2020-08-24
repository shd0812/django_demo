"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appone import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^publisher_list/', views.publisher),
    url(r'^publisher_add/', views.add),
    url(r'^publisher_delete/', views.publisher_delete),
    url(r'^publisher_edit/', views.publisher_edit),



    url(r'^book_list/', views.book_list),
    url(r'^book_add/', views.book_add),
    url(r'^book_del/', views.book_del),
    url(r'^book_edit/', views.book_edit),



    url(r'^author_list/', views.author_list),
    url(r'^author_add/', views.author_add),
    url(r'^author_del/', views.author_del),
    url(r'^author_edit/', views.author_edit),



]
