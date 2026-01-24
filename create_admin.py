import os
import django

# 1. Configuration pour que Django comprenne qu'on est dans le projet
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mon_portfolio.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# 2. Tes identifiants Admin
USERNAME = "admin"
EMAIL = "admin@portfolio.com"
PASSWORD = "admin123" 

# 3. La logique : On crée le compte seulement s'il n'existe pas
if not User.objects.filter(username=USERNAME).exists():
    print(f"🚀 Création automatique du superutilisateur : {USERNAME}")
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
else:
    print("✅ L'admin existe déjà.")

