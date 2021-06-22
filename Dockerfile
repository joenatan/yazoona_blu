FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN apt update && apt install libmagic-dev netcat libpq-dev gcc -y
RUN pip install pipenv && pipenv install --system

COPY . /app/

EXPOSE 8000
