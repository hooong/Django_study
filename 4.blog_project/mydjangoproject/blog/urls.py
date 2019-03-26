from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name='new'),
    path('create/', views.create, name="create"),
    path('newblog/', views.blogpost, name="newblog"),
    path('<int:blog_pk>/comment_new', views.comment_write, name="comment_write"),
    # path('<int:pk>/like', views.post_like, name='post_like'),
]