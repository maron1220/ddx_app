import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = '5wup%g1&8g0m$55k0+r&51elua-6h86dkh0p^%9e*w4&cng+38'

DEBUG = True
