from django.conf.urls import url

from listimoveis.login.views import new, call_logout

urlpatterns = [
    url(r'^$', new, name='login'),
    url(r'^logout/$', call_logout, name='logout'),
]