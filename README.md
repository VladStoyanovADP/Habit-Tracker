# Habit-Tracker

# Install python3-django

psql -f setup-db.sql

pip install djangorestframework

python3 -m venv .venv

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py loaddata test_data.json

python3 manage.py runserver


