FROM python:3.10-slim

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh app.py /app/


ENTRYPOINT [ "/app/entrypoint.sh" ]