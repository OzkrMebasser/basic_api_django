from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path('add/', views.add_tour),
    path('users/', views.get_users),
    path('add_user/', views.add_user)
]