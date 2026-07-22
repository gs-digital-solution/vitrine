from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = RichTextField(verbose_name="Description")
    image = models.ImageField(upload_to='products/', verbose_name="Image principale")
    video_url = models.URLField(blank=True, null=True, verbose_name="Lien vidéo (YouTube/Facebook...)")
    playstore_url = models.URLField(blank=True, null=True, verbose_name="Lien Play Store")
    priority = models.PositiveIntegerField(default=0, verbose_name="Priorité (plus grand = plus visible)")
    is_published = models.BooleanField(default=True, verbose_name="Publié")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")

    class Meta:
        ordering = ['-priority', '-created_at']
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery/', verbose_name="Photo")
    title = models.CharField(max_length=100, blank=True, verbose_name="Légende")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['order']
        verbose_name = "Photo du produit"
        verbose_name_plural = "Photos des produits"

    def __str__(self):
        return f"Photo de {self.product.title}"

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = RichTextField(verbose_name="Description")
    image = models.ImageField(upload_to='services/', verbose_name="Image d'illustration")
    priority = models.PositiveIntegerField(default=0, verbose_name="Priorité (plus grand = plus visible)")
    is_published = models.BooleanField(default=True, verbose_name="Publié")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")

    class Meta:
        ordering = ['-priority', '-created_at']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='services/gallery/', verbose_name="Photo")
    title = models.CharField(max_length=100, blank=True, verbose_name="Légende")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['order']
        verbose_name = "Photo du service"
        verbose_name_plural = "Photos des services"

    def __str__(self):
        return f"Photo de {self.service.title}"

class Achievement(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=200, verbose_name="Titre de la réalisation")
    client_name = models.CharField(max_length=200, verbose_name="Nom du client")
    image = models.ImageField(upload_to='achievements/', verbose_name="Image du projet")
    project_url = models.URLField(blank=True, null=True, verbose_name="Lien vers le projet")
    description = models.TextField(blank=True, verbose_name="Description courte")

    class Meta:
        verbose_name = "Réalisation"
        verbose_name_plural = "Réalisations"

    def __str__(self):
        return f"{self.title} - {self.client_name}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Prénom")
    message = models.TextField(verbose_name="Message")
    is_published = models.BooleanField(default=False, verbose_name="Publié sur le site")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de soumission")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"

    def __str__(self):
        return f"Témoignage de {self.name} ({'publié' if self.is_published else 'en attente'})"

class SiteConfig(models.Model):
    # On utilise un singleton : une seule ligne pour toute la configuration du site
    company_name = models.CharField(max_length=100, default="Mon Agence", verbose_name="Nom de l'agence")
    hero_title = models.CharField(max_length=200, default="Bienvenue sur notre site", verbose_name="Titre de la bannière")
    hero_subtitle = models.TextField(default="Nous vous accompagnons dans votre transformation digitale", verbose_name="Sous-titre de la bannière")
    hero_cta_text = models.CharField(max_length=50, default="Découvrir nos services", verbose_name="Texte du bouton CTA")
    hero_cta_url = models.CharField(max_length=200, default="#services", verbose_name="Lien du bouton CTA")
    about_text = RichTextField(blank=True, null=True, verbose_name="Texte 'À propos'")
    address = models.CharField(max_length=255, blank=True, verbose_name="Adresse")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    email = models.EmailField(blank=True, verbose_name="Email")
    # Réseaux sociaux
    facebook_url = models.URLField(blank=True, null=True, verbose_name="Lien Facebook")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="Lien LinkedIn")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Lien Instagram")
    youtube_url = models.URLField(blank=True, null=True, verbose_name="Lien YouTube")
    tiktok_url = models.URLField(blank=True, null=True, verbose_name="Lien TikTok")
    telegram_url = models.URLField(blank=True, null=True, verbose_name="Lien Telegram")
    # contact whatsapp direct
    whatsapp_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Numéro WhatsApp (ex: 237691xxxxxx)"
    )
    whatsapp_message = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Message pré-défini (optionnel)",
        help_text="Message qui s'affichera à l'ouverture de la conversation WhatsApp"
    )
    footer_copyright = models.CharField(max_length=200, default="© 2026 - Tous droits réservés", verbose_name="Copyright dans le footer")
    # pour changer les couleurs du site depuis le dashboard
    primary_color = ColorField(
        default='#0d6efd',
        verbose_name="Couleur principale (boutons, bannières)"
    )
    secondary_color = ColorField(
        default='#0a58ca',
        verbose_name="Couleur secondaire (dégradés, survols)"
    )
    # pour changer le thème du site de manière dynamique
    THEME_CHOICES = [
        ('classic', 'Classique (sobre et professionnel)'),
        ('modern', 'Moderne (couleurs vives, ombres)'),
        ('elegant', 'Élégant (polices fines, tons pastel)'),
    ]

    theme_choice = models.CharField(
        max_length=20,
        choices=THEME_CHOICES,
        default='classic',
        verbose_name="Thème du site"
    )
    class Meta:
        verbose_name = "Configuration du site"
        verbose_name_plural = "Configuration du site"

    def __str__(self):
        return "Configuration générale"

    def save(self, *args, **kwargs):
        # On s'assure qu'il n'y ait qu'une seule ligne dans la table
        if not self.pk and SiteConfig.objects.exists():
            raise ValueError("Il existe déjà une configuration. Modifiez-la directement.")
        super().save(*args, **kwargs)

    @classmethod
    def get_config(cls):
        """Récupère ou crée l'unique instance de configuration"""
        config, created = cls.objects.get_or_create(id=1)
        return config

class VisitorCounter(models.Model):
    total_visits = models.PositiveIntegerField(
        default=0,
        verbose_name="Nombre total de visites"
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Compteur de visiteurs"
        verbose_name_plural = "Compteur de visiteurs"

    def __str__(self):
        return f"{self.total_visits} visiteurs"

    @classmethod
    def get_counter(cls):
        """Récupère ou crée l'unique instance du compteur"""
        counter, created = cls.objects.get_or_create(id=1)
        return counter

    @classmethod
    def increment(cls):
        """Incrémente le compteur de 1"""
        counter = cls.get_counter()
        counter.total_visits += 1
        counter.save()
        return counter.total_visits