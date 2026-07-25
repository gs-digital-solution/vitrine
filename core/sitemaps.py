from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, Service

class StaticSitemap(Sitemap):
    """Sitemap pour les pages statiques (accueil, à propos, contact)"""
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['home', 'about', 'products', 'services']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    """Sitemap pour les produits"""
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Product.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class ServiceSitemap(Sitemap):
    """Sitemap pour les services"""
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Service.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at