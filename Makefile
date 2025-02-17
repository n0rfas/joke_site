format:
	isort backend
	ruff format backend

check:
	isort --check-only backend
	ruff check backend
	mypy backend

tests:
	pytest

run:
	fastapi dev backend/app/main.py
