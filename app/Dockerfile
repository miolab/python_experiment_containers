FROM python:3.8.6-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY pyproject.toml ./

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
  build-essential \
  curl \
  git \
  gzip \
  inotify-tools \
  ssh \
  sudo \
  tar \
  vim

RUN pip install --upgrade pip

RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install
