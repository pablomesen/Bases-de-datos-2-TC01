FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
