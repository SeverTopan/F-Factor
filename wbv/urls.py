from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.WbvEntryList.as_view(), name='list'),
]