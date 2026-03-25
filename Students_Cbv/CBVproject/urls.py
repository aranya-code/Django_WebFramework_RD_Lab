"""
URL configuration for CBVproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from CBVApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.studentInfoView.as_view(), name='student'),
    path('<int:pk>/', views.studentDetailsView.as_view(),name='detail'),
    path('create/', views.studentCreateView.as_view(), name= 'create'),
    path('update/<int:pk>/', views.studentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.studentDeleteView.as_view(), name='delete'),
]
