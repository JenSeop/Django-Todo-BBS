from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('post/', views.todo_post, name='todo_post'),
]