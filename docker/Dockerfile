FROM python:3.10-alpine3.16

ENV PYTHONUNBUFFERED=1

COPY ./requirements/requirements.txt /requirements/requirements.txt
COPY ./app /app

WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements/requirements.txt

ENV PATH="/scripts:/py/bin:$PATH"