from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ThpEntryList.as_view(), name='list'),
]