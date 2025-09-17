import os
from .settings import *

# Production settings for PythonAnywhere
DEBUG = False

# Replace 'yourusername' with your actual PythonAnywhere username
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# Database for production (MySQL on PythonAnywhere)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$labourdb',
        'USER': 'yourusername',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Static files
STATIC_ROOT = '/home/yourusername/mysite/static'
MEDIA_ROOT = '/home/yourusername/mysite/media'

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Change this to a secure secret key
SECRET_KEY = 'your-production-secret-key-here-make-it-long-and-random'