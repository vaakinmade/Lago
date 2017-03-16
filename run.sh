#!/bin/bash
# Create a virtualenv
virtualenv --python=python3.4 LagoApp
# Activate the virtualenv
source LagoApp/bin/activate
# Install project Python packages
pip install -r requirements.txt
# Setup required environment variables
export DJANGO_SETTINGS_MODULE=config.settings.local
export DATABASE_URL=postgres://jenkins:jenkins@localhost/jenkins
# Apply migrations
./manage.py migrate
# Run the django-jenkins management command
./manage.py jenkins --enable-coverage --coverage-html-report=htmlcov --coverage-rcfile .coveragerc --max-complexity 10
# Delete the virtualenv
rm -rf LagoApp