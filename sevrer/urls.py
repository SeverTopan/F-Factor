from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='Admin'),
    url(r'^todo/', include('todo.urls'), name='ToDo')
]
