from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='Admin'),
    url(r'^update/', include('update.urls'), name='update'),
    url(r'^leaders/', include('leaders.urls'), name='leaders'),
    url(r'^wbv/', include('wbv.urls'), name='wbv'),
]
