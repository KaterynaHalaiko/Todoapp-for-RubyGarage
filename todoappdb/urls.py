from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView, TemplateView

from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.groups import GroupAddView, GroupUpdateView, \
    GroupDeleteView, groups_list
from students.views.journal import JournalView

from .settings import MEDIA_ROOT, DEBUG


js_info_dict = {
    'packages': ('task',),
}

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'task.views.task.task_list', name='home'),
    url(r'^task/add/$', 'task.views.task.task_add',
        name='task_add'),
    url(r'^task/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(),
        name='task_edit'),
    url(r'^task/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(),
        name='task_delete'),

    # Groups urls
    url(r'^project/$', login_required(groups_list), name='project'),
    url(r'^project/add/$', login_required(GroupAddView.as_view()),
        name='project_add'),
    url(r'^project/(?P<pk>\d+)/edit/$',
        login_required(GroupUpdateView.as_view()),
        name='project_edit'),
    url(r'^project/(?P<pk>\d+)/delete/$',
        login_required(GroupDeleteView.as_view()),
        name='project_delete'),

    # Journal urls
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    # Contact Admin Form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin',
        name='contact_admin'),

    # User Related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(
        template_name='registration/profile.html')), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},
        name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

    # Social Auth Related urls
    url('^social/', include('social.apps.django_app.urls', namespace='social')),

    url(r'^jsi18n\.js$', 'django.views.i18n.javascript_catalog', js_info_dict),

    url(r'^admin/', include(admin.site.urls)),

)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))
