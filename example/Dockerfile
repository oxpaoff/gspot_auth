FROM python:3.11-slim-buster

ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

WORKDIR /app
COPY ./requirements.txt /app/

# Project initialization:
RUN pip install -r requirements.txt

# Creating folders, and files for a project:
COPY . /app


CMD python manage.py runserver 0.0.0.0