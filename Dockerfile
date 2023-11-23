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

# handler for machine learning
RUN ppip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cpu --no-cache-dir

ADD . /app/
RUN pip install poetry charset-normalizer easyocr --no-cache-dir
RUN poetry install