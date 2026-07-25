from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import (HomeView, ProductListView, ServiceListView,
                        TestimonialCreateView, ProductDetailView, ServiceDetailView,AboutView)
from core.views import manifest_view

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
