"""
Django settings for pineapple project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a23vukslfng-f39jo_=%@76a73ofgbg0x@6s-yc8-u!q@$8mhn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Seems 'testserver needs to be here for unit testing:
ALLOWED_HOSTS = ['testserver', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz',
    'unitTests'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pineapple.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pineapple.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#MySQL config. For at denne skal fynke, må du ha laget en lokal database med rett navn og privilegier.
#Kort guide, det er antatt at mysql er installert og at du har laget en root konto:
    #åpne CMD
    #Logg inn på MySQL som administrator:
        # mysql -u root -p
        #(Skriv inn passord)
    #Lag ny database med navn "pinedatabase":
        #CREATE DATABASE pinedatabase CHARACTER SET utf8;
    #Gi databasen rett privilegier (username og passord er "admin":
        #GRANT ALL PRIVILEGES ON pinedatabase.* To 'admin'@'127.0.0.1' IDENTIFIED BY 'admin';

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'pinebase.db'),
    }
}
'''
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'pinedatabase',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'OPTIONS': {
          'autocommit': True,
        }
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

# Login page
LOGIN_URL = '/login/' #  Url der innlogging skjer
LOGIN_REDIRECT_URL = '/' #  Url som det redirectes til etter successfull innlogging