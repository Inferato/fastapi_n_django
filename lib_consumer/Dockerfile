FROM python:3.12-slim

WORKDIR /app

COPY ./lib_cunsumer/lib_c /app/lib_c
COPY ./lib_cunsumer/lib_c/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/lib_c

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
