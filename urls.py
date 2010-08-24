from django.conf.urls.defaults import *
from django.contrib.flatpages.models import FlatPage
from django.contrib.sitemaps import FlatPageSitemap
from django.contrib import admin
from django.conf import settings

from calloway.urls import urlpatterns as calloway_patterns

admin.autodiscover()

sitemaps = {
    'flatpages': FlatPageSitemap,
}

urlpatterns = patterns('',
  (r'^account/',include('registration.urls')),
  (r'^admin/', include(admin.site.urls)),
  (r'^contact/$','mail.views.contact'),
  (r'^stream-waders/$', 'mail.views.streamwader'),
  (r'^survey/$', 'mail.views.survey'),
  (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
    )

urlpatterns += calloway_patterns[1:]

