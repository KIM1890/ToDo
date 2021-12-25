from django.contrib import admin
from django.urls import path,include

urlpatterns =[
    #home pages
    path('',include('todo.urls')),
    path('admin/',admin.site.urls)
]