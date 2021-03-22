FROM python:3
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN pip install wheel
RUN pip install -r requirements/docker.txt
ENV DJANGO_SETTINGS_MODULE=network_inventory.settings.local
RUN python manage.py collectstatic --noinput
CMD ["/bin/bash", "/code/run.sh"]
