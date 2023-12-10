from django.urls import path

from project import views

urlpatterns = [
    path('one', views.one_login),
    path('two', views.two_login),
    path('five', views.five_login),
]