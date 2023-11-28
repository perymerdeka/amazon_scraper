FROM library/python:3.11.0

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


ADD . /app/
RUN pip install poetry charset-normalizer --no-cache-dir
RUN poetry install

RUN pip install torch --index-url https://download.pytorch.org/whl/nightly/cpu --no-cache-dir
RUN pip install torchvision==0.2.2.post3 --no-cache-dir
RUN pip install easyocr --no-cache-dir