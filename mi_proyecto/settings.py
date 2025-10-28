from pathlib import Path
import os

# 📁 Base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Clave secreta (no compartas esto en producción)
SECRET_KEY = 'django-insecure-nf)5k_#u(pen)^!wb$o9s7$h-929%_4$9up!93z_18+5^l+^9g'

# ⚙️ Modo producción
DEBUG = False
ALLOWED_HOSTS = ['mi-proyecto-django-5788.onrender.com']

# 📦 Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Tu aplicación principal
]

# 🧱 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 Configuración de URLs
ROOT_URLCONF = 'mi_proyecto.urls'

# 🧩 Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚀 WSGI
WSGI_APPLICATION = 'mi_proyecto.wsgi.application'

# 🗄️ Base de datos PostgreSQL (Render usa variables de entorno, pero aquí está la versión local)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mi_proyecto_django',
        'USER': 'postgres',
        'PASSWORD': 'rootdb',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# 🔐 Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌎 Internacionalización
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# 🖼️ Archivos estáticos
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 📷 Archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🧬 Clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
