from django.contrib import admin
from .models import Category, Region, ContentPage, RedirectRule

admin.site.register(Category)
admin.site.register(Region)
admin.site.register(ContentPage)
admin.site.register(RedirectRule)
