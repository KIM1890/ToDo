from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todo'),
    path('del/<int:task_id>', views.remove, name='del'),
    path('edit/<int:task_id>', views.update, name='edit'),
]
