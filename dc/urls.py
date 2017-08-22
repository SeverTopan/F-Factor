from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DcEntryList.as_view(), name='list'),
]