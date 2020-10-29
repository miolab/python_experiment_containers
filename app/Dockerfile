FROM python:3.8.6-slim

WORKDIR /app
COPY pyproject.toml ./

ENV PYTHONUNBUFFERED=1

RUN apt-get update -y && \
  apt-get upgrade -y && \
  apt-get install -y --no-install-recommends \
  build-essential \
  curl \
  git \
  inotify-tools \
  vim
RUN apt-get clean

RUN pip install --upgrade pip

# Install: Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install
