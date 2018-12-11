from django.conf.urls import url
from django.contrib.auth import views as auth_views

from s3metafora.core import views


urlpatterns = [
    url(r'^$', views.upload, name='home'),
    url(r'^filelist$', views.filelist, name='filelist'),
    url(r'^logout$', views.log_out, name='log_out'),
    url(r'^registermember$', views.register, name='register'),
]
