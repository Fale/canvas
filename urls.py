from django.conf.urls import patterns, url
from canvas.views import canvas, item

urlpatterns = patterns('',
    url(r'^$', canvas.index, name='index'),
    url(r'^add/$', canvas.addCanvas, name='addCanvas'),
    url(r'^(?P<canvas_id>\d+)/$', canvas.canvas, name='canvas'),
    url(r'^(?P<canvas_id>\d+)/edit/$', canvas.editCanvas, name='editCanvas'),
    url(r'^(?P<canvas_id>\d+)/delete/$', canvas.deleteCanvas, name='deleteCanvas'),
    url(r'^(?P<canvas_id>\d+)/add/(?P<box>\w+)/$', item.addItem, name='addItem'),
    url(r'^(?P<canvas_id>\d+)/(?P<item_id>\d+)/delete/$', item.deleteItem, name='deleteItem'),
    url(r'^(?P<canvas_id>\d+)/(?P<item_id>\d+)/edit/$', item.editItem, name='editItem'),
)
