from django.conf.urls import patterns, url
from canvas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<canvas_id>\d+)/$', views.canvas, name='canvas')
)
