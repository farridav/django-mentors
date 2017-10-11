#!/bin/sh

# Start Gunicorn processes
cd /app/
echo Starting Gunicorn.
exec gunicorn mentors.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3