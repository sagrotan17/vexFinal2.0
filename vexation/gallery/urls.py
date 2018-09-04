from django.conf.urls import url


from .sitemaps import GallerySitemap
from django.contrib.sitemaps.views import sitemap


from . import views

sitemaps = {
    'galleries': GallerySitemap,
}

urlpatterns = [

    url(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^(?P<pk>\d+)/(?P<gallery_slug>[-\w]+)/$', views.gallery_detail, name = 'gallery_detail'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.gallery_by_category, name='gallery_by_category'),

    url(r'^$', views.gallery_home, name='gallery_home'),


    ]
