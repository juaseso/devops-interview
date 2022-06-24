FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
# FROM python:3.7

ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app/

# Copy requirements.txt case it doesn't exist in the repo
COPY ./app/requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./app /app
ENV PYTHONPATH=/app
