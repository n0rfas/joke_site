#!/bin/sh

source .venv/bin/activate

echo "Waiting for database..."
sleep 3  # We give time to start Postgres

echo "We are performing migrations..."
alembic -c ./migrations/alembic.ini upgrade head

echo "Launching FastAPI..."
exec uvicorn app.main:app --host 0.0.0.0 --port 80
