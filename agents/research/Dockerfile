FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

COPY agents/research/requirements.txt /app/agents/research/requirements.txt
RUN pip install --no-cache-dir -r /app/agents/research/requirements.txt

COPY shared /app/shared
COPY agents/research /app/agents/research

EXPOSE 8000

CMD ["uvicorn", "agents.research.app:app", "--host", "0.0.0.0", "--port", "8000"]
