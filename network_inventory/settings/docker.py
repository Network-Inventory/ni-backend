from .base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'backend',
]

base_url = os.environ.get('NI_BASE_URL')
if base_url:
    ALLOWED_HOSTS.append(base_url)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = os.environ.get('DJANGO_DEBUG')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
        'PASSWORD': 'password',
    }
}
