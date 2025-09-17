#!/usr/bin/env python
"""
Setup script for Labour Attendance Management System
Run this script to initialize the database and create a master user
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_project():
    """Initialize the Django project"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labour_management.settings')
    django.setup()
    
    print("Setting up Labour Attendance Management System...")
    
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
    
    print("\nSetup completed successfully!")
    print("\nLogin credentials:")
    print("   Username: master")
    print("   Password: master123")
    print("\nTo start the server, run:")
    print("   python manage.py runserver")

if __name__ == '__main__':
    setup_project()