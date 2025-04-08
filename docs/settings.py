# Minimal Django settings for documentation building
# This file is used by sphinx-build to import and autodoc the Django package

SECRET_KEY = 'django-admin-collaborator-docs'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'django_admin_collaborator',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    }
}

# Settings for django-admin-collaborator
ADMIN_COLLABORATOR_REDIS_URL = 'redis://localhost:6379/0'