FROM python:3.11.2-alpine3.17

LABEL maintainer Francis J. Garcia <contacto@francisjgarcia.es>
LABEL org.opencontainers.image.source="https://github.com/francisjgarcia/autodeskargas_scraper_api"
LABEL org.opencontainers.image.description "API scraper for forums which are posted movies and series in Spanish. The scraper is written in Python and uses Scrapy to parse the HTML and extract the data. The API is written in Django and uses Django REST Framework to expose the data."

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN addgroup -S python && adduser -S python -G python

USER python:python

WORKDIR /usr/src/app

COPY --chown=python:python app .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py" ]

CMD [ "runserver", "0.0.0.0:8000" ]
