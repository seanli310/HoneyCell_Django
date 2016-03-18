__author__ = 'jianheluo'

from django.conf.urls import include, url
from . import views

from django.conf import settings
from django.conf.urls.static import static

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

    # new task page
    url(r'^newTask/$', 'WebApp.views.newTask', name='newTask'),

    #create new task instance
    url(r'^create_new_task/$', 'WebApp.views.create_new_task', name='create_new_task'),

    # history tasks page
    url(r'^historyTask/$', 'WebApp.views.historyTask', name='historyTask'),

    # folder Management page
    url(r'^fileManage/$', 'WebApp.views.fileManage', name='fileManage'),
    url(r'^fileManage_tasks/$', 'WebApp.views.fileManage_tasks', name='fileManage_tasks'),

    # profile tasks page
    url(r'^profile/$', 'WebApp.views.profile', name='profile'),

    # settings page
    url(r'^settings/$', 'WebApp.views.settings', name='settings'),

    # follow other users
    url(r'^add_followship/(?P<user_id>\d+)$', 'WebApp.views.follow', name='follow'),

    # unfollow other users
    url(r'^delete_followship/(?P<user_id>\d+)$', 'WebApp.views.unfollow', name='unfollow'),

    # new user guide page
    url(r'^guide/$', 'WebApp.views.guide', name='guide'),

    # global_page
    url(r'^global_page/$', 'WebApp.views.global_page', name='global_page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)