compile:
	uv pip compile --all-extras pyproject.toml -o requirements/dev.txt

format:
	ruff check --select I --fix .
	ruff format .

check:
	ruff check --select I .
	ruff check .
	mypy .

test:
	pytest -vv

run:
	# fastapi dev app/main.py
	uvicorn app.main:app --reload --port 8000

migrate:
	alembic upgrade head

migrate-create:
	alembic revision --autogenerate -m "$(name)"

migrate-downgrade:
	alembic downgrade -1

clean:
	find . -name __pycache__ -exec rm -rf {} +
	find . -name "*.py[co]" -o -name .pytest_cache -exec rm -rf {} +
	find . -type d -empty -delete