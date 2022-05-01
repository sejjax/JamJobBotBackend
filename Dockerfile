FROM python:3.9-buster
ENV BOT_NAME=$BOT_NAME

WORKDIR /usr/src/app/"${BOT_NAME:-tg_bot}"

RUN apt update
RUN pip install poetry

COPY requirements.txt /usr/src/app/"${BOT_NAME:-tg_bot}"
RUN pip3 install -r /usr/src/jamjobbotbackend/"${BOT_NAME:-tg_bot}"/pyproject.toml
COPY . /usr/src/app/"${BOT_NAME:-tg_bot}"
