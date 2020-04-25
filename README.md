# Recipes app REST API

[![Build Status](https://travis-ci.org/alpden550/recipes-app-api.svg?branch=master)](https://travis-ci.org/alpden550/recipes-app-api)

Recipes app based on the Django REST Framework.

The authorized user could create tags, ingredients, and recipes include image uploading.

All available methods for user and recipes can find on the [swagger page](http://127.0.0.1:8000/swagger/)

[![swagger.png](https://i.postimg.cc/cC1Q3pbP/swagger.png)](https://postimg.cc/2bJbRKmx)

Or on the [redoc page](http://127.0.0.1:8000/redoc/)


## How to install

Download code or clone it from Github, and install dependencies.

Create .env file and type:

````bash
POSTGRES_USER=postgres user
POSTGRES_PASSWORD=postgres password
DEBUG=true if needed
SECRET_KEY=exrtra secret key
````

Or pass env variables via docker run.

## How to run local

```bash
docker-compose up
```
