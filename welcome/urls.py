from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome),
    path('welcome/', views.welcome)
]
