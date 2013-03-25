from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('integration.views',
    url(r'^$', 'index', name='index'),
    url(r'^load/$', 'load', name='load'),
    url(r'^export/$', 'export', name='export'),

    url(r'^new/$', 'new', name='new'),
    url(r'^edit/(\d+)/$', 'edit', name='edit'),
    url(r'^delete/(\d+)$', 'delete', name='delete'),
    url(r'^detail/(\d+)$', 'detail', name='detail'),
)
