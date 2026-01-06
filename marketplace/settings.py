from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-1v%-h!97gez1#@a*ck^kh#cm47nrt5&%(j*(ze@#=8-5a+ph2&"

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    "p4-thomas-vehicle-marketplace-cf589c4c8f97.herokuapp.com",
    "localhost",
    "127.0.0.1",
]

INSTALLED_APPS = [
    "cloudinary",
    "cloudinary_storage",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "products",
    "accounts",
    "checkout",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "marketplace.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "marketplace.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dlkst7boo',
    'API_KEY': '<397568769876832>',
    'API_SECRET': '<C40qTxWIZvZMt9lh4uEP03sVF3w>'
}


if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

WHITENOISE_MANIFEST_STRICT = False


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
