from django.contrib import admin
from django.urls import path, include

from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('registration/', views.reg),
    path('login/', views.login),
path('mails/', include('project.urls')),
path('logins/', include('project.urls_logins')),

]
