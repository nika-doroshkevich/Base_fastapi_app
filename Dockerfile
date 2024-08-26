FROM python:3.11.4

RUN mkdir /example-base-app

WORKDIR /example-base-app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY . .

RUN chmod a+x docker/*.sh

WORKDIR example-base-app