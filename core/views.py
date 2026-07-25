from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Product, Service, Testimonial, SiteConfig, VisitorCounter
from .forms import TestimonialForm
from django.http import JsonResponse

# ========================================
# PAGE D'ACCUEIL
# ========================================
class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_config'] = SiteConfig.get_config()
        context['products'] = Product.objects.filter(is_published=True)[:3]
        context['services'] = Service.objects.filter(is_published=True)[:3]
        context['testimonials'] = Testimonial.objects.filter(is_published=True)[:6]
        context['visitor_count'] = VisitorCounter.get_counter().total_visits
        return context


# ========================================
# LISTE DES PRODUITS
# ========================================
class ProductListView(ListView):
    model = Product
    template_name = 'core/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_config'] = SiteConfig.get_config()
        context['visitor_count'] = VisitorCounter.get_counter().total_visits
        return context


# ========================================
# LISTE DES SERVICES
# ========================================
class ServiceListView(ListView):
    model = Service
    template_name = 'core/services.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_config'] = SiteConfig.get_config()
        context['visitor_count'] = VisitorCounter.get_counter().total_visits
        return context


# ========================================
# SOUMISSION D'UN TÉMOIGNAGE
# ========================================
class TestimonialCreateView(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'core/testimonial_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Merci ! Votre témoignage a été envoyé pour validation.")
        return response

# ========================================
# DÉTAIL D'UN PRODUIT
# ========================================
from django.views.generic import DetailView  # Assurez-vous que cette ligne est en haut du fichier

class ProductDetailView(DetailView):
    model = Product
    template_name = 'core/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_config'] = SiteConfig.get_config()
        context['visitor_count'] = VisitorCounter.get_counter().total_visits
        return context


# ========================================
# DÉTAIL D'UN SERVICE
# ========================================
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'core/service_detail.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_config'] = SiteConfig.get_config()
        context['visitor_count'] = VisitorCounter.get_counter().total_visits
        return context
# ========================================
# VUE POUR RECUPERER LE NOM DU CLIENT POUR PWA SUR MOBILE
# ========================================
def manifest_view(request):
    config = SiteConfig.get_config()
    return JsonResponse({
        "name": config.company_name,
        "short_name": config.company_name,
        "description": f"Site vitrine de {config.company_name}",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#0d6efd",
        "orientation": "portrait-primary",
        "icons": [
            {"src": "/static/icons/icon-192.png", "type": "image/png", "sizes": "192x192"},
            {"src": "/static/icons/icon-512.png", "type": "image/png", "sizes": "512x512"}
        ]
    })