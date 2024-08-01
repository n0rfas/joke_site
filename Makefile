format:
	ruff format backend

check:
	ruff check backend
	mypy backend

tests:
	pytest
