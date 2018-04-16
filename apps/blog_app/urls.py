from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^new$', views.new), # anything that comes in with "new"
    url(r'^create$', views.create), # anything that comes in with "create"
    url(r'^(?P<number>\d+)$', views.show),# anything from that comes in with a number
    url(r'^(?P<number>\d+)/edit', views.edit), # anything from the root with number/edit path
    url(r'^(?P<number>\d+)/delete', views.destroy)
]   