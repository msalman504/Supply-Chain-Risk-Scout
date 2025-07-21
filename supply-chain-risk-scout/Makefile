install:
	pip install -r requirements.txt

lint:
	ruff check src && black --check src

test:
	pytest

dev:
	docker-compose up --build 