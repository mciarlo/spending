import os

# Directories
# The app path lives one directory above settings
APP_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '..'))

# The project directory lives one directory above the app
PROJECT_DIR = os.path.normpath(os.path.join(APP_DIR, '..'))

TEMPLATE_DIRS = (
    os.path.join(APP_DIR, 'templates'),
    APP_DIR,
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(APP_DIR, 'static'),
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'tastypie',
    'gunicorn',
    'main',
    'accounts',
)

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

ROOT_URLCONF = 'main.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': APP_DIR + '/db.sqlite',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'WARNING',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(APP_DIR, 'log', 'spending.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'propagate': True,
            'level': 'DEBUG',
        }
    }
}
