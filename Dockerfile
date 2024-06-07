FROM python:3.10.0-slim

RUN mkdir docker_demo
WORKDIR docker_demo

COPY requirements.txt /docker_demo/

COPY . /docker_demo/

COPY .docker.env /docker_demo/.env
RUN pip install -r requirements.txt
RUN python -m pip install --upgrade pip
ENV APP=DOCKER_DEMO

