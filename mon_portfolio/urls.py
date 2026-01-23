from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vitrine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('profil/', views.apropos, name='apropos'),
    path('formation/', views.formation, name='formation'),
    path('experience/', views.experience, name='experience'),
    path('certificats/', views.certificats, name='certificats'),
    path('projets/', views.projets, name='projets'),
    path('contact/', views.contact, name='contact'),
]

# Ajoute ce bloc magique pour les images :
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # ... (laisse tout le code du haut comme il est) ...

# PERSONNALISATION DE L'ADMIN
admin.site.site_header = "Administration Portfolio"
admin.site.site_title = "Admin Mouhamed Diouf"
admin.site.index_title = "Bienvenue dans votre espace de gestion"