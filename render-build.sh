#!/usr/bin/env bash
# Exit on error -- this is for render
set -o errexit



# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
cd ./django_site
# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

