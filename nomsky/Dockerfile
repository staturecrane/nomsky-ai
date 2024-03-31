FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .

RUN python -m pip install -U pip
RUN python -m pip install -r requirements.txt

COPY . .