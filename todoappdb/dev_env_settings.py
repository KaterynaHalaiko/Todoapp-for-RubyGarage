### WARNING!: do not keep this file in repository;
### create it from sample_env_setting.py every time on every new
### server and fill in proper settings for that new environment

### Do not modify next 2 lines
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

### You can modify below settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        # 'USER': 'students_db_user',
        # 'PASSWORD': 'password',
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'todoapp_db',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$lrm#z+qs)(&2rkr)tnui0m0%7r%)s!)9ni$#ug_vjmce+5x%!'

# website root url
PORTAL_URL = 'http://localhost:8000'

# email settings
ADMIN_EMAIL = 'admin@todoapp.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_PASSWORD = '********'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# static and media resources
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

# facebook API Keys
SOCIAL_AUTH_FACEBOOK_KEY = '**********'
SOCIAL_AUTH_FACEBOOK_SECRET = '***********************'
