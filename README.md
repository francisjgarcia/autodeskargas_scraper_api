# AutoDesKargaS (Scraper API)

## Table of contents

- [AutoDesKargaS (Scraper API)](#autodeskargas-scraper-api)
  - [Table of contents](#table-of-contents)
  - [Description](#description)
    - [Websites scraped](#websites-scraped)
  - [Usage](#usage)
    - [Set environment variables](#set-environment-variables)
      - [Docker compose](#docker-compose)
      - [Application](#application)
    - [Build and run container](#build-and-run-container)
  - [Using API](#using-api)
    - [Movies](#movies)
      - [Get movies](#get-movies)
      - [Get specific movie quality](#get-specific-movie-quality)
      - [Push thanks button](#push-thanks-button)
      - [Get download urls](#get-download-urls)
      - [Add new comment to post in forum](#add-new-comment-to-post-in-forum)
    - [Series](#series)

## Description

API scraper for forums which are posted movies and series in Spanish. The scraper is written in Python and uses Scrapy to parse the HTML and extract the data. The API is written in Django and uses Django REST Framework to expose the data.

### Websites scraped

- [DescargasDD](https://descargasdd.org/)

## Usage

### Set environment variables

#### Docker compose

The docker compose file uses the environment variables to build the container. The environment variables are defined in the file `.env` in the folder `deployments`.

```bash
COMPOSE_PROJECT_NAME=autodeskargas # Name of the project
# API movie environment variables
SCRAPER_MOVIES_EXPOSE_PORT=autodeskargas_scraper_movies # Name of the image to build of movies API scraper
SCRAPER_MOVIES_EXPOSE_PORT=8000 # Port exposed by the container
# API series environment variables
SCRAPER_SERIES_EXPOSE_PORT=autodeskargas_scraper_series # Name of the image to build of series API scraper
SCRAPER_SERIES_EXPOSE_PORT=8001 # Port exposed by the container
```

#### Application

The application uses the environment variables. The environment variables are defined in the file `.env` in the folder `app`.

```bash
# Django settings
SECRET_KEY=s3cr3t_k3y # Django secret key
DEBUG=True # Django debug mode (True or False)
ALLOWED_HOSTS=* # Django allowed hosts (comma separated)

# Scraping type
SCRAPY_TYPE=movies # Set scraping type (movies or series)

# Scraping DescargasDD
BASE_URL=https://descargasdd.org # Base url of the forum
WEB_USER=username # Username of the forum 
WEB_PASSWORD=p4ssw0rd # Password of the forum
# Scraping always or only news
SCRAPY_ALWAYS=True # Scrapy always all posts of forum (True or False)
```

### Build and run container

There are two ways to run the container.
The first one is to build the container and run it.

To build the container of movies API scraper, you can execute the following commands:
```bash
cd autodeskargas_scraper_api

docker build -f deployments/Dockerfile -t autodeskargas_scraper_movies .

docker run -d --name autodeskargas_scraper_movies --env-file app/.env -p 8000:8000 autodeskargas_scraper_movies 
```

To build the container of series API scraper, you can execute the following commands:
```bash
cd autodeskargas_scraper_api

docker build -f deployments/Dockerfile -t autodeskargas_scraper_series .

docker run -d --name autodeskargas_scraper_series --env-file app/.env -p 8001:8001 autodeskargas_scraper_series 
```


The second one is execute the docker-compose file.

If you want to run both containers for movies and series, you can execute the following commands:
```bash
cd autodeskargas_scraper_movies/deployments

docker-compose up -d
```

Or if you want to run only one container, you can execute the following commands:

To run only the container of movies API scraper:
```bash
cd autodeskargas_scraper_movies/deployments

docker-compose up -d autodeskargas_scraper_movies
```

To run only the container of series API scraper:
```bash
cd autodeskargas_scraper_series/deployments

docker-compose up -d autodeskargas_scraper_series
```

## Using API

### Movies

#### Get movies

To get all movies, you can consume the endpoint `/api/v1/movies` with the method `GET`.

```bash
curl -X GET http://localhost:8000/api/v1/movies
```

#### Get specific movie quality

To get a specific movie quality, you can consume the endpoint `/api/v1/movies` with the method `POST` and the body:

```json
{
    "quality": "<quality>"
}
```

Where `<quality>` is the quality of the movie. The possible values are:

- `micro1080`
- `bdrip1080`
- `h265`
- `4k`
- `animation_micro1080`
- `animation_bdrip1080`
- `animation_h265`
- `animation_4k`
- `anime_micro1080`
- `anime_micro1080_vose`
- `anime_bdrip1080`
- `anime_bdrip1080_vose`
- `anime_h265`
- `anime_h265_vose`

```bash
curl -X POST http://localhost:8000/api/v1/movies \
    -H 'Content-Type: application/json' \
    -d '{"quality": "<quality>"}'
```

#### Push thanks button

Before get the download urls of the movies, you need to push the thanks button. To do this, you can consume the endpoint `/api/v1/thanks` with the method `POST` and the body:

For example:
```json
{
    "link": 12345
}
```

Where `<link>` is the url ID of the movie in the forum.

```bash
curl -X POST http://localhost:8000/api/v1/thanks \
    -H 'Content-Type: application/json' \
    -d '{"link": <link>}'
```

#### Get download urls

To get the download urls of the movies, you can consume the endpoint `/api/v1/download_urls` with the method `POST` and the body:

For example:
```json
{
    "link": 12345
}
```

Where `<link>` is the url ID of the movie in the forum.

```bash
curl -X POST http://localhost:8000/api/v1/download_urls \
    -H 'Content-Type: application/json' \
    -d '{"link": <link>}'
```

#### Add new comment to post in forum

To add a new comment to a post in the forum, you can consume the endpoint `/api/v1/comments` with the method `POST` and the body:

For example:
```json
{
    "link": 12345,
    "comment": "This is a comment"
}
```

Where `<link>` is the url ID of the movie in the forum and `<comment>` is the message to add to the post.

```bash
curl -X POST http://localhost:8000/api/v1/comments \
    -H 'Content-Type: application/json' \
    -d '{"link": <link>, "comment": "<comment>"}'
```

### Series
