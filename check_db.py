#!/usr/bin/env python
"""
Database check script for production deployment
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labour_management.settings')
django.setup()

from users.models import User

def check_database():
    try:
        # Check if master user exists
        master_user = User.objects.filter(username='master').first()
        if master_user:
            print("✅ Master user exists")
            print(f"   Username: {master_user.username}")
            print(f"   Role: {master_user.role}")
        else:
            print("❌ Master user not found")
            print("   Creating master user...")
            User.objects.create_user(
                username='master',
                password='master123',
                email='master@system.com',
                role='master',
                is_staff=True,
                is_superuser=True,
                force_password_change=False
            )
            print("✅ Master user created")
        
        # Check total users
        total_users = User.objects.count()
        print(f"📊 Total users in database: {total_users}")
        
        return True
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

if __name__ == '__main__':
    print("Checking database...")
    if check_database():
        print("✅ Database check completed")
    else:
        print("❌ Database check failed")