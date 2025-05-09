FROM python:3.12

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*p

RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    mysql-connector-python \
    future \
    pyparsing

WORKDIR /app

COPY src/ ./src
COPY conf/ ./conf

CMD ["python", "/app/src/python/main.py"]