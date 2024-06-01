FROM python:3.10-slim

WORKDIR usr/src/app

COPY requirements/prod.txt .
RUN pip install -r prod.txt
COPY . .
COPY .docker.env ./.env

RUN python manage.py collectstatic --noinput