from django.conf.urls import url
from django.urls import path, re_path

from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from .feeds import LatestPostsFeed

from . import views


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [


    url(r'^category/(?P<category_slug>[-\w]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^(?P<pk>\d+)/(?P<post_slug>[-\w]+)$', views.post_detail, name='post_detail'),
    #url(r'^$', views.post_list,  name='post_list'),

    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    url(r'^blog/comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^blog/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    url(r'^$', views.blog_home, name='blog_home'),
]


