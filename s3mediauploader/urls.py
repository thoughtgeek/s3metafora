from django.conf.urls import url
from django.contrib.auth import views as auth_views

from s3mediauploader.core import views


urlpatterns = [
    url(r'^$', views.upload, name='home'),
    url(r'^filelist$', views.filelist, name='filelist'),
]
