from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'test_smartLabelS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thank-you/$', 'test_smartLabelS.views.thankyou', name='thankyou'),
    url(r'^learn-more/$', 'test_smartLabelS.views.learnmore', name='learnmore'),
    url(r'^login/$', 'test_smartLabelS.views.login'),
    url(r'^auth/$', 'test_smartLabelS.views.auth_view'),
    url(r'^logout/$', 'test_smartLabelS.views.logout'),
    url(r'^loggedin/$', 'test_smartLabelS.views.loggedin'),
    url(r'^invalid/$', 'test_smartLabelS.views.invalid_login'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
