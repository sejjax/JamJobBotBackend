FROM python:3.9
ENV APP_NAME=$APP_NAME
ENV APP_MODE=$APP_MODE

WORKDIR /usr/src/app

RUN apt update
RUN apt install systemd -y
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml /usr/src/app
RUN poetry install
COPY . /usr/src/app

RUN systemctl enable /usr/src/app/systemd/app.service
