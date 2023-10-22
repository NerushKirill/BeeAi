app:
	poetry run uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
dev_stand:
	docker-compose -f ./docker-compose-dev.yaml up -d
test:
	poetry run coverage run -m pytest .
	poetry run coverage html
	poetry run black ./
	poetry run ruff check --fix .
#	poetry run mypy ./
#	poetry run pylint ./src
migrations:
#	alembic init migrations
#	alembic init -t async migrations
	alembic revision --autogenerate -m "make migrations"
	alembic upgrade heads
build:
	docker build . --tag bee_ai
# 	docker run --p 8000:8000 bee_ai
up:
	docker-compose -f ./docker-compose-local.yaml up -d
down:
	docker-compose -f ./docker-compose-local.yaml down && docker network prune --force
