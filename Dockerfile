FROM python:3.9-slim

WORKDIR /app

COPY src/ ./src

CMD ["python", "/app/src/main.py"]