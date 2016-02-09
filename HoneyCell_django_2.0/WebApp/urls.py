__author__ = 'jianheluo'

from django.conf.urls import include, url
from . import views


urlpatterns = [

    # empty url
    url(r'^$', 'WebApp.views.index', name='index'),

    url(r'^index/$', 'WebApp.views.index', name='index'),

    # new argument 'template_name'
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'WebApp/login.html'}, name='login'),

    # url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'WebApp.views.my_logout', name='logout'),

    # registration is normal route
    url(r'^registration/$', 'WebApp.views.registration', name='registration'),

]