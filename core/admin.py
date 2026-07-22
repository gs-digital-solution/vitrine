from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Product, ProductImage, Service, ServiceImage, Achievement,
    Testimonial, SiteConfig, VisitorCounter
)

# ========================================
# PRODUITS (avec galerie)
# ========================================
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    fields = ['image', 'title', 'order']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'is_published', 'created_at', 'image_preview']
    list_editable = ['priority', 'is_published']
    list_filter = ['is_published', 'priority']
    search_fields = ['title', 'description']
    inlines = [ProductImageInline]
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'priority', 'is_published')
        }),
        ('Médias', {
            'fields': ('image', 'video_url', 'playstore_url')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit:cover; border-radius:4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Aperçu"


# ========================================
# SERVICES (avec galerie et réalisations)
# ========================================
class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 3
    fields = ['image', 'title', 'order']

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 2
    fields = ['title', 'client_name', 'image', 'project_url', 'description']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'is_published', 'created_at', 'image_preview']
    list_editable = ['priority', 'is_published']
    list_filter = ['is_published', 'priority']
    search_fields = ['title', 'description']
    inlines = [ServiceImageInline, AchievementInline]
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'priority', 'is_published')
        }),
        ('Médias', {
            'fields': ('image',)
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit:cover; border-radius:4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Aperçu"


# ========================================
# TÉMOIGNAGES
# ========================================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'message_preview', 'created_at', 'is_published']
    list_editable = ['is_published']
    list_filter = ['is_published', 'created_at']
    search_fields = ['name', 'message']
    actions = ['publish_testimonials', 'unpublish_testimonials']

    def message_preview(self, obj):
        return obj.message[:60] + "..." if len(obj.message) > 60 else obj.message
    message_preview.short_description = "Extrait du message"

    def publish_testimonials(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"{updated} témoignage(s) ont été publiés.")
    publish_testimonials.short_description = "Publier les témoignages sélectionnés"

    def unpublish_testimonials(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f"{updated} témoignage(s) ont été dépubliés.")
    unpublish_testimonials.short_description = "Dépublier les témoignages sélectionnés"


# ========================================
# CONFIGURATION DU SITE (Singleton)
# ========================================
@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_cta_text', 'hero_cta_url')
        }),
        ('À propos', {
            'fields': ('about_text',)
        }),
        ('Coordonnées', {
            'fields': ('company_name', 'address', 'phone', 'email')
        }),
        ('Réseaux sociaux', {
            'fields': ('facebook_url', 'linkedin_url', 'instagram_url', 'youtube_url', 'tiktok_url', 'telegram_url')
        }),
        ('Design / Thèmes', {
            'fields': ('theme_choice',)
        }),
        ('Footer', {
            'fields': ('footer_copyright',)
        }),
        ('Personnalisation des couleurs', {  # <-- Nouveau fieldset pour les couleurs
            'fields': ('primary_color', 'secondary_color')
        }),
        ('WhatsApp', {
            'fields': ('whatsapp_number', 'whatsapp_message')
        }),
    )

    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

# ========================================
# COMPTEUR DE VISITEURS (Lecture seule)
# ========================================
@admin.register(VisitorCounter)
class VisitorCounterAdmin(admin.ModelAdmin):
    list_display = ['total_visits']
    readonly_fields = ['total_visits']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        return []