# BUILD
FROM python:3.15-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --target=/app -r requirements.txt

COPY app.py .

# RUNTIME 
FROM cgr.dev/chainguard/python:latest

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 8000

CMD ["app.py"]