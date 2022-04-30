import asyncio
import logging
from flask import Flask
from telethon import TelegramClient

from app.config import load_config
from app.controllers import register_auth_controller
from app.services import AuthService

logger = logging.getLogger(__name__)


def register_all_controllers(tgclient: TelegramClient, httpserver: Flask):
    register_auth_controller(httpserver, AuthService(tgclient))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting application")
    config = load_config(".env")

    tgclient = TelegramClient()
    httpserver = Flask()
    # start
    httpserver.run()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
