#!/bin/sh

set -e

echo "Waiting for PostgreSQL..."
while ! python -c "import psycopg2, os; psycopg2.connect(host=os.environ.get('POSTGRES_HOST','db'), port=os.environ.get('POSTGRES_PORT','5432'), user=os.environ.get('POSTGRES_USER','postgres'), password=os.environ.get('POSTGRES_PASSWORD','postgres'), dbname=os.environ.get('POSTGRES_DB','postgres')).close()" 2>/dev/null; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 1
done
echo "PostgreSQL is up!"

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec "$@"
