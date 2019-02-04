from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:img_id>/', views.view, name='view'),
]