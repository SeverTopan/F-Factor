from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ToDoList.as_view(), name='list'),
]