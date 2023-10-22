FROM python:3.11.6-alpine3.18

EXPOSE 8000

WORKDIR /app

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install poetry

COPY . /app

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev


CMD ["poetry", "run", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
