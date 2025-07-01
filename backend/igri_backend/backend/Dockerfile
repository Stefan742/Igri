FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

CMD ["daphne", "igri_backend.asgi:application", "-b", "0.0.0.0", "-p", "8000"]
