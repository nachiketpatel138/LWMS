#!/usr/bin/env python
"""
Deployment setup script for PythonAnywhere
Run this after uploading your project to PythonAnywhere
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_production():
    """Initialize the Django project for production"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labour_management.settings_production')
    django.setup()
    
    print("Setting up Labour Management System for Production...")
    
    # Run migrations
    print("\nCreating database tables...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create master user
    print("\nCreating master user...")
    execute_from_command_line(['manage.py', 'create_master_user'])
    
    # Collect static files
    print("\nCollecting static files...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    print("\nProduction setup completed successfully!")
    print("\nLogin credentials:")
    print("   Username: master")
    print("   Password: master123")

if __name__ == '__main__':
    setup_production()