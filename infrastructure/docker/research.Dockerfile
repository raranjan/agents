FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/shared:/app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY shared /app/shared
COPY agents /app/agents

EXPOSE 8000

CMD ["uvicorn", "agents.research.app:app", "--host", "0.0.0.0", "--port", "8000"]
