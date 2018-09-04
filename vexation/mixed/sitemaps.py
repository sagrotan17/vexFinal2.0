from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from django.urls import reverse
from .urls import urlpatterns as mixedUrls

class MixedSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        url_list = []
        for url in mixedUrls:
            url_list.append('mixed:' +url.name)
        return url_list

    def location(self, item):
        return reverse(item)