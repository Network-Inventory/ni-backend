from .base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'backend',
]

ni_host = os.environ.get('NI_HOST')
if ni_host:
    ALLOWED_HOSTS.append(ni_host)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False
if os.environ.get('NI_MODE') == "development":
    DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    }
}
