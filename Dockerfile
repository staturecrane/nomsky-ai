FROM python:3.10-slim

RUN apt update
RUN apt install watchman

WORKDIR /app

COPY requirements.txt .
COPY requirements_dev.txt .

RUN python -m pip install -r requirements.txt
RUN python -m pip install -r requirements_dev.txt

COPY ./.pyre_configuration .
COPY ./nomsky nomsky