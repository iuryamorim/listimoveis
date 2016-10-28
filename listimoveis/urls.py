from django.conf.urls import url, include
from django.contrib import admin

from listimoveis.core.views import home, search

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^$', search, name='search'),
    #url(r'^(?P<search>[\w-]+)/$', search, name='search'),
    url(r'^login/', include('listimoveis.login.urls', namespace='login')),
    url(r'^imoveis/', include('listimoveis.imoveis.urls', namespace='imoveis')),

    url(r'^admin/', admin.site.urls),
]
