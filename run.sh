#!/bin/bash
sleep 2
python manage.py makemigrations backups
python manage.py makemigrations computers
python manage.py makemigrations core
python manage.py makemigrations customers
python manage.py makemigrations devices
python manage.py makemigrations licenses
python manage.py makemigrations nets
python manage.py makemigrations softwares
python manage.py makemigrations users
python manage.py makemigrations
python manage.py migrate

if $(python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"); then
    python manage.py loaddata backups
    python manage.py loaddata computers
    python manage.py loaddata core
    python manage.py loaddata devices
    python manage.py loaddata nets
    python manage.py loaddata softwares
fi
find . \( -name __pycache__ -o -name "*.pyc" \) -delete
gunicorn network_inventory.wsgi:application --reload --bind 0.0.0.0:8000 --workers 3
