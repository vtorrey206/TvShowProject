from django.conf.urls import url
from . import views
from .models import Shows

                    
urlpatterns = [
     url(r'^shows$', views.shows),
     url(r'^shows/new$', views.new),
     url(r'^shows/create$', views.create),
     url(r'^shows/(?P<id>\d+)$', views.info),
     url(r'^shows/(?P<id>\d+)/edit$', views.edit),
     url(r'^shows/(?P<id>\d+)/update$', views.update),
     url(r'^shows/(?P<id>\d+)/delete$', views.delete),
]