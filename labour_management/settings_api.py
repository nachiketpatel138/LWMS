from .settings import *
import os

# API-only settings
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# CORS for frontend
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOWED_ORIGINS = [
    "https://your-app.web.app",  # Replace with Firebase URL
    "http://localhost:3000",     # React dev
    "http://localhost:4200",     # Angular dev
]

# API responses only
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

# Remove template/static settings for API
TEMPLATES = []
STATICFILES_DIRS = []
STATIC_ROOT = None