from django.conf.urls import url

from listimoveis.imoveis.views import new, detail, alter, update, delete

urlpatterns = [
    url(r'^$', new, name='imoveis'),
    url(r'^(?P<slug>[\w-]+)/$', detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/alter$', alter, name='alter'),
    url(r'^(?P<slug>[\w-]+)/alter/salve$', update, name='alter'),
    url(r'^(?P<slug>[\w-]+)/delete$', delete, name='delete'),
]