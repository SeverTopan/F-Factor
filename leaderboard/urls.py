from django.conf.urls import include, url
from django.contrib import admin
from leaderboard import views

urlpatterns = [
    url(r'^$', views.leaderboard, name='leaderboard'),
]

