from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyFirstDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    
    # urls for app "news"
    url(r'^meldungen/$', 'news.views.meldungen'),
    url(r'^meldungen/(?P<meldungs_id>\d+)/$', 'news.views.meldung_detail'),
)
