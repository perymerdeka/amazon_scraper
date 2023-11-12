FROM library/python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt update -y

RUN mkdir /app

RUN ls /app
WORKDIR /app

RUN pip install --upgrade pip

ADD . /app/
RUN pip install poetry
RUN poetry install