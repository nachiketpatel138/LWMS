# Render Deployment Guide

## Step 1: Push to GitHub
1. Create a new repository on GitHub
2. Push your project:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/labour-management.git
git push -u origin main
```

## Step 2: Deploy on Render
1. Go to [render.com](https://render.com) and sign up/login
2. Click "New" → "Blueprint"
3. Connect your GitHub repository
4. Render will automatically detect `render.yaml` and create:
   - Web Service (Django app)
   - PostgreSQL Database

## Step 3: Environment Variables (Auto-configured)
- `DATABASE_URL` - Auto-generated from PostgreSQL service
- `SECRET_KEY` - Auto-generated secure key
- `WEB_CONCURRENCY` - Set to 4 for performance

## Step 4: Access Your App
- Your app will be available at: `https://labour-management.onrender.com`
- Login with: `master` / `master123`

## Manual Deployment (Alternative)
If you prefer manual setup:

1. **Create Web Service:**
   - Build Command: `./build.sh`
   - Start Command: `gunicorn labour_management.wsgi:application`
   - Environment: Python 3

2. **Create PostgreSQL Database:**
   - Name: `labour-db`
   - Plan: Free

3. **Connect Database:**
   - Add `DATABASE_URL` environment variable from database

## Important Notes:
- Free tier has limitations (sleeps after 15 minutes of inactivity)
- Database has 1GB storage limit on free tier
- Static files served by WhiteNoise
- Automatic HTTPS enabled

## Troubleshooting:
- Check build logs for errors
- Ensure `build.sh` has execute permissions
- Verify all dependencies in requirements.txt