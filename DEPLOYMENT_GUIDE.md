# PythonAnywhere Deployment Guide

## Quick Setup Commands

### 1. After uploading and extracting your project:
```bash
cd ~
python3.10 -m venv mysite-env
source mysite-env/bin/activate
cd mysite
pip install -r requirements_production.txt
```

### 2. Update settings_production.py with your details:
- Replace `yourusername` with your PythonAnywhere username
- Replace `your_mysql_password` with your MySQL password
- Generate a new SECRET_KEY

### 3. Initialize database:
```bash
python deployment_setup.py
```

### 4. Web App Configuration:
- **Source code:** `/home/yourusername/mysite`
- **Working directory:** `/home/yourusername/mysite`
- **Virtualenv:** `/home/yourusername/mysite-env`
- **Static files URL:** `/static/` → `/home/yourusername/mysite/static/`
- **Media files URL:** `/media/` → `/home/yourusername/mysite/media/`

### 5. WSGI Configuration:
Copy content from `wsgi.py` to your PythonAnywhere WSGI file.

## Login Credentials:
- **Username:** master
- **Password:** master123

## Important Notes:
1. Create MySQL database: `yourusername$labourdb`
2. Update ALLOWED_HOSTS in settings_production.py
3. Set DEBUG = False for production
4. Generate secure SECRET_KEY
5. Reload web app after changes

## File Upload Permissions:
```bash
chmod 755 /home/yourusername/mysite/media
chmod 755 /home/yourusername/mysite/media/templates
chmod 755 /home/yourusername/mysite/media/upload_errors
```

## Troubleshooting:
- Check error logs in Web tab
- Ensure all paths use your actual username
- Verify database credentials
- Check static files are collected properly