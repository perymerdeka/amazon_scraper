import os

from .base import *

# Database Settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PWD', ''),
        'HOST': os.environ.get("DB_HOST", ),  # Sesuaikan dengan host PostgreSQL Anda
        'PORT': os.environ.get("DB_PORT"),      # Sesuaikan dengan port PostgreSQL Anda
    }
}



