#!/bin/sh
echo "Waiting for postgres..."
while ! nc -z db 5432; do
    sleep 0.1
done
echo "PostgreSQL started"

# Initialize DB 
python manage.py flush --no-input
python manage.py migrate
python manage.py loaddata podcast_player/fixtures/users.json

exec "$@"