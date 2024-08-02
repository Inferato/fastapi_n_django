FROM python:3.12-slim

WORKDIR /app

COPY ./store/lib_store /app/lib_store
COPY ./store/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["bash", "-c", "uvicorn lib_store.main:app --host 0.0.0.0 --port 9000"]
