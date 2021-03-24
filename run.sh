#!/bin/bash
sleep 2
python manage.py migrate

if $(python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"); then
    python manage.py loaddata backups
    python manage.py loaddata computers
    python manage.py loaddata core
    python manage.py loaddata devices
    python manage.py loaddata nets
    python manage.py loaddata softwares
fi
gunicorn network_inventory.wsgi:application --reload --bind 0.0.0.0:8000 --workers 3
