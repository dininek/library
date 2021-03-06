from django.conf.urls import patterns, include, url
from filebrowser.sites import site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^library/', include('library.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
  	url(r'^chaining/', include('smart_selects.urls')),
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/filebrowser/', include(site.urls)),	

)
