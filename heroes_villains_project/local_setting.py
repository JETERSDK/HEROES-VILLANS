# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-182yer4&g#8012dh4km62)mqwtz!eawb8)uza1a4g3$garp$cj'



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'M@ximu$70',
    }
}