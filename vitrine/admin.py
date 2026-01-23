from django.contrib import admin
from django.utils.html import format_html
from .models import Projet, ContactMessage, Lieu, Competence, Certificat, Experience

# 1. PROJETS
@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('apercu_image', 'titre', 'outils')
    def apercu_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "-"

# 2. COMPÉTENCES (Modifiable directement dans la liste !)
@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'niveau_visuel', 'niveau')
    list_editable = ('niveau',) # Tu pourras changer les % sans ouvrir la fiche !
    
    def niveau_visuel(self, obj):
        # Affiche une petite barre de progression dans l'admin
        return format_html(
            '<div style="width:100px; background:#e0e0e0; border-radius:5px;">'
            '<div style="width:{}%; background:#0ca789; height:10px; border-radius:5px;"></div>'
            '</div>', 
            obj.niveau
        )
    niveau_visuel.short_description = "Barre"

# 3. CERTIFICATS
@admin.register(Certificat)
class CertificatAdmin(admin.ModelAdmin):
    list_display = ('titre', 'organisme', 'date_obtention')
    list_filter = ('organisme',)

# 4. EXPÉRIENCES & FORMATIONS
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('poste_ou_diplome', 'categorie', 'structure', 'date_debut')
    list_filter = ('categorie',) # Filtre pour voir soit Pro, soit Études

# 5. MESSAGES
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'date_envoi')
    readonly_fields = ('nom', 'email', 'message', 'date_envoi')
    def has_add_permission(self, request): return False

# 6. LIEUX
@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'latitude', 'longitude')