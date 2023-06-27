# Overview

GSpot Auth is a Django app for GSpot project https://github.com/DJWOMS/GSpot

Quick start
-----------

1. Add "gspot_auth" to your INSTALLED_APPS setting like this:

```
INSTALLED_APPS = [
    ...
    'gspot_django_auth',
]
```

2. Define these parameters in `settings.py`

- `REDIS_ACCESS_PREFIX`
- `REDIS_ACCESS_DB`
- `REDIS_HOST`
- `REDIS_PORT`
- `REDIS_PASSWORD`
- `GET_TOKEN_FROM` - 'headers' or 'cookies'

2. Add CustomJWTAuthentication to DEFAULT_AUTHENTICATION_CLASSES in settings.py

```
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'gspot_django_auth.authentication.CustomJWTAuthentication'
    ],
}
```
