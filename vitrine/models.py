from django.db import models

# 1. TES PROJETS
class Projet(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/')
    outils = models.CharField(max_length=200, help_text="Ex: Python, Django, QGIS")
    lien = models.URLField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

# 2. TES COMPÉTENCES (C'est celle-ci qui manquait !)
class Competence(models.Model):
    nom = models.CharField(max_length=50, help_text="Ex: Python, Analyse Spatiale")
    niveau = models.IntegerField(default=80, help_text="Pourcentage de maîtrise (0 à 100)")
    icone_code = models.CharField(max_length=50, default="fas fa-check", blank=True, help_text="Code FontAwesome")

    def __str__(self):
        return self.nom

# 3. TES CERTIFICATS
class Certificat(models.Model):
    titre = models.CharField(max_length=100)
    organisme = models.CharField(max_length=100)
    date_obtention = models.DateField()
    lien_preuve = models.URLField(blank=True, null=True)
    image_logo = models.ImageField(upload_to='certificats/', blank=True, null=True)

    def __str__(self):
        return self.titre

# 4. TON PARCOURS (EXPÉRIENCES & FORMATIONS)
class Experience(models.Model):
    TYPE_CHOICES = (
        ('PRO', 'Expérience Pro'),
        ('EDU', 'Formation / Études'),
    )
    categorie = models.CharField(max_length=3, choices=TYPE_CHOICES, default='PRO')
    poste_ou_diplome = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-date_debut']

    def __str__(self):
        return f"{self.poste_ou_diplome} chez {self.structure}"

# 5. MESSAGES REÇUS
class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.nom}"

# 6. CARTE
class Lieu(models.Model):
    nom = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.nom