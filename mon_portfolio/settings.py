"""
Django settings for mon_portfolio project.
"""

from pathlib import Path
import os 
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o^ly4)gfq$e5gsy@_+^_2&$yh!a26bv)u-m5bpwab*o5&*)c!^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Pour la mise en ligne, on autorise tous les hébergeurs
ALLOWED_HOSTS = ['*']


# Application definition
# J'ai fusionné tes listes : Jazzmin est bien en premier !
INSTALLED_APPS = [
    'jazzmin',                  # <--- DOIT ETRE EN PREMIER
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vitrine',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mon_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Correction ici (plus propre)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mon_portfolio.wsgi.application'


# =========================================
# BASE DE DONNÉES (HYBRIDE) 🧠
# =========================================

# Par défaut : SQLite (pour ton ordinateur)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Si on est sur Render (c'est-à-dire si une adresse de base de données existe)
# On écrase la config par défaut pour utiliser Neon (PostgreSQL)
database_url = os.environ.get("DATABASE_URL")
if database_url:
    DATABASES["default"] = dj_database_url.parse(database_url)


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'fr-fr' # J'ai mis en Français pour toi

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# =========================================
# FICHIERS STATIQUES ET MEDIAS (VERSION PROD)
# =========================================

STATIC_URL = '/static/'

# Dossier de travail (où tu codes)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# --- CE QU'IL MANQUAIT POUR LA PRODUCTION (CRITIQUE) ---
# Dossier où Django rassemble les fichiers pour le serveur
STATIC_ROOT = BASE_DIR / "staticfiles"

# Le moteur de Whitenoise pour compresser et servir les fichiers
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# -------------------------------------------------------

# Pour les images uploadées (projets)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================================
# CONFIGURATION EMAIL (GMAIL)
# =========================================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'dioufmouhamed959@gmail.com'
EMAIL_HOST_PASSWORD = 'dvvj bhim sgtb jfih'


# ====================================
# CONFIGURATION JAZZMIN (DESIGN ADMIN)
# ====================================
JAZZMIN_SETTINGS = {
    "site_title": "Admin Portfolio",
    "site_header": "Espace Mouhamed",
    "site_brand": "Mouhamed Diouf",
    "welcome_sign": "Bienvenue dans ton cockpit de pilotage",
    "copyright": "Mouhamed Diouf - 2026",
    "topmenu_links": [
        {"name": "Voir le site",  "url": "accueil", "permissions": ["auth.view_user"]},
    ],
    "search_model": "vitrine.Projet",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-primary",
}