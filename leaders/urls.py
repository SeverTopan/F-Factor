from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.LeaderView.as_view(), name='list'),
    url(r'^wbv/$', views.WbvLeaderView.as_view(), name='wbv'),
    url(r'^bm/$', views.BmLeaderView.as_view(), name='bm'),
    url(r'^oc/$', views.OcLeaderView.as_view(), name='oc'),
    url(r'^thp/$', views.ThpLeaderView.as_view(), name='thp'),
    url(r'^dc/$', views.DcLeaderView.as_view(), name='dc'),
]