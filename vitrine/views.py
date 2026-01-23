from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
# J'ajoute les imports manquants ici (Competence, Experience, Certificat) 👇
from .models import Projet, ContactMessage, Lieu, Competence, Experience, Certificat

def accueil(request):
    # On peut afficher les 3 derniers projets sur l'accueil par exemple
    derniers_projets = Projet.objects.all().order_by('-date_creation')[:3]
    return render(request, 'index.html', {'projets': derniers_projets})

def apropos(request):
    # C'EST ICI QUE LA MAGIE DU GRAPHIQUE OPÈRE ✨
    competences = Competence.objects.all()
    
    # On prépare les listes pour le Javascript (Chart.js)
    skill_names = [c.nom for c in competences]
    skill_levels = [c.niveau for c in competences]

    context = {
        'competences': competences,
        'skill_names': skill_names,   # Indispensable pour le graphique
        'skill_levels': skill_levels, # Indispensable pour le graphique
    }
    return render(request, 'apropos.html', context)

def formation(request):
    # On récupère seulement les expériences de type 'EDU' (Education)
    formations = Experience.objects.filter(categorie='EDU').order_by('-date_debut')
    return render(request, 'formation.html', {'formations': formations})

def experience(request):
    # On récupère seulement les expériences de type 'PRO' (Travail)
    experiences = Experience.objects.filter(categorie='PRO').order_by('-date_debut')
    return render(request, 'experience.html', {'experiences': experiences})

def certificats(request):
    # On récupère tous les certificats
    mes_certificats = Certificat.objects.all().order_by('-date_obtention')
    return render(request, 'certificats.html', {'certificats': mes_certificats})

def projets(request):
    tous_les_projets = Projet.objects.all().order_by('-date_creation')
    return render(request, 'projets.html', {'projets': tous_les_projets})

def contact(request):
    # 1. Gestion du Formulaire (Emails)
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email_visiteur = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(nom=nom, email=email_visiteur, message=message)

        # Envoi des emails
        try:
            sujet = f"Nouveau message Portfolio de {nom}"
            message_complet = f"Nom : {nom}\nEmail : {email_visiteur}\n\nMessage :\n{message}"
            send_mail(sujet, message_complet, email_visiteur, ['dioufmouhamed959@gmail.com'], fail_silently=False)
            send_mail("Confirmation - Mouhamed Diouf", f"Bonjour {nom}, bien reçu !", 'dioufmouhamed959@gmail.com', [email_visiteur], fail_silently=True)
        except:
            pass

        messages.success(request, "Merci ! Votre message a bien été envoyé.")
        return redirect('contact')

    # 2. Gestion de la Carte
    tous_les_lieux = list(Lieu.objects.values('nom', 'latitude', 'longitude', 'description'))

    return render(request, 'contact.html', {'lieux': tous_les_lieux})