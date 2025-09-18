import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labour_management.settings')

# Setup Django
django.setup()

# Get WSGI application
application = get_wsgi_application()

# For compatibility with default Render setup
app = application