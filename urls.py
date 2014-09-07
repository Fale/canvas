from django.conf.urls import patterns, url
from canvas.views import canvas, item, logout

urlpatterns = patterns('',
    url(r'^$', canvas.list, name='listCanvas'),
    url(r'^add/$', canvas.add, name='addCanvas'),
    url(r'^(?P<canvas_id>\d+)/$', canvas.show, name='showCanvas'),
    url(r'^(?P<canvas_id>\d+)/edit/$', canvas.edit, name='editCanvas'),
    url(r'^(?P<canvas_id>\d+)/delete/$', canvas.delete, name='deleteCanvas'),
    url(r'^(?P<canvas_id>\d+)/add/(?P<box>\w+)/$', item.add, name='addItem'),
    url(r'^(?P<canvas_id>\d+)/(?P<item_id>\d+)/delete/$', item.delete, name='deleteItem'),
    url(r'^(?P<canvas_id>\d+)/(?P<item_id>\d+)/edit/$', item.edit, name='editItem'),
)
