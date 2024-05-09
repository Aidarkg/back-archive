FROM python:3.10.0-slim

RUN mkdir docker_demo
WORKDIR docker_demo

COPY requirements.txt /docker_demo/
RUN pip install -r requirements.txt
COPY . /docker_demo/

COPY .docker.env /docker_demo/.env
ENV APP=DOCKER_DEMO

RUN python manage.py makemigrations faq moderator data_media
RUN python manage.py migrate