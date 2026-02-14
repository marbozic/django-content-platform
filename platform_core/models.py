from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ContentPage(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft"
        PUBLISHED = "published"

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    title = models.CharField(max_length=160)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    noindex = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.category}-{self.region}")
        if self.status == self.Status.PUBLISHED:
            self.noindex = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class RedirectRule(models.Model):
    source = models.CharField(max_length=255, unique=True)
    target = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.source} -> {self.target}"
