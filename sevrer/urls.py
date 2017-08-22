from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='Admin'),
    url(r'^update/', include('update.urls'), name='update'),
    url(r'^leaders/', include('leaders.urls'), name='leaders'),
    url(r'^wbv/', include('wbv.urls'), name='wbv'),
    url(r'^thp/', include('thp.urls'), name='thp'),
    url(r'^oc/', include('oc.urls'), name='oc'),
    url(r'^dc/', include('dc.urls'), name='dc'),
    url(r'^bm/', include('bm.urls'), name='bm'),
]
