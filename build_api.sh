#!/usr/bin/env bash
set -o errexit

pip install -r requirements_api.txt
python manage.py migrate
python manage.py create_master_user