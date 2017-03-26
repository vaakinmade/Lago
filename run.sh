#!/bin/bash
PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv" ]; then
        virtualenv venv
fi
. venv/bin/activate

# Install project Python packages
pip install -r requirements.txt

# Run the django-jenkins management command
python manage.py jenkins --enable-coverage
