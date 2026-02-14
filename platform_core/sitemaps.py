from django.contrib.sitemaps import Sitemap
from .models import ContentPage

class ContentSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return ContentPage.objects.filter(status=ContentPage.Status.PUBLISHED)

    def location(self, obj):
        return f"/{obj.slug}/"
