from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import (HomeView, ProductListView, ServiceListView,
                        TestimonialCreateView, ProductDetailView, ServiceDetailView,AboutView)
from core.views import manifest_view
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticSitemap, ProductSitemap, ServiceSitemap
from django.views.generic import TemplateView
from core.views import google_verify



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('a-propos/', AboutView.as_view(), name='about'),
    path('produits/', ProductListView.as_view(), name='products'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('temoignage/', TestimonialCreateView.as_view(), name='testimonial_add'),
    path('produits/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('manifest.json', manifest_view, name='manifest'),
]

# Sitemap
sitemaps = {
    'static': StaticSitemap,
    'products': ProductSitemap,
    'services': ServiceSitemap,
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]


urlpatterns += [
    path('google5901fe031a3697b7.html', google_verify, name='google_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

