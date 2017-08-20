from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.LeaderView.as_view(), name='list'),
]