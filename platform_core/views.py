from django.shortcuts import get_object_or_404, render
from django.core.cache import cache
from .models import ContentPage

def page_view(request, slug):
    cache_key = f"page:{slug}"
    page = cache.get(cache_key)

    if not page:
        page = get_object_or_404(ContentPage, slug=slug, status=ContentPage.Status.PUBLISHED)
        cache.set(cache_key, page, 60)

    return render(request, "platform_core/page.html", {"page": page})
