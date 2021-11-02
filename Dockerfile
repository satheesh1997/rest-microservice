FROM python:alpine3.9

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    mariadb-dev

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install gunicorn

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 micro:app
