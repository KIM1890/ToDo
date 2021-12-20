from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='task'),
    path('del/<int:item_id>', views.remove(), name='del')
    # path('del/<int:item_id>', views.remove, name='del'),
]
