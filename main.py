#!/usr/bin/env python3

import asyncio
import logging
from flask import Flask
from telethon import TelegramClient

from app.config import load_config
from app.controllers import register_auth_controller

logger = logging.getLogger(__name__)


def register_all_controllers(client: TelegramClient, httpserver: Flask):
    register_auth_controller(client, httpserver)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting application")
    config = load_config(".env")

    client = TelegramClient(
        session='temp/session_id.session',
        api_id=config.tg_bot.api_id,
        api_hash=config.tg_bot.api_hash
    )

    httpserver = Flask(__name__)

    register_all_controllers(client, httpserver)

    # start
    try:
        await client.connect()
        httpserver.run(
            host=config.httpserver.host,
            port=config.httpserver.port,
        )
    finally:
        await client.disconnect()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
