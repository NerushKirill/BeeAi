app:
	poetry run uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
test:
	poetry run coverage run -m pytest .
	poetry run coverage html
	poetry run black ./
	poetry run ruff check --fix .
#	poetry run mypy ./
#	poetry run pylint ./src
migrations:
	poetry run alembic init -t async alembic
	poetry run alembic upgrade heads
	poetry run alembic revision --autogenerate -m "Create DB"
build:
	docker build . --tag bee_ai
# 	docker run --p 8000:8000 bee_ai
up:
	docker-compose -f ./docker-compose-local.yaml up -d
down:
	docker-compose -f ./docker-compose-local.yaml down && docker network prune --force

