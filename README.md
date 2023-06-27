# Overview

GSpot Auth is a Django app for GSpot project https://github.com/DJWOMS/GSpot

Quick start
-----------

1. Add "gspot_auth" to your INSTALLED_APPS setting like this:

```
INSTALLED_APPS = [
    ...
    'gspot_auth',
]
```

2. Add CustomJWTAuthentication to DEFAULT_AUTHENTICATION_CLASSES in settings.py

```
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'gspot_auth.authentication.CustomJWTAuthentication'
    ],
}
```