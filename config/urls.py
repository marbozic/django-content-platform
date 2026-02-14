from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from platform_core.sitemaps import ContentSitemap

sitemaps = {"content": ContentSitemap}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("platform_core.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
]
