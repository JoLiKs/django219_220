from django.urls import path

from project import views

urlpatterns = [
    path('', views.mails),
    path('one', views.one),
    path('two', views.two),
]