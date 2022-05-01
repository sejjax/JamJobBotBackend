from telethon import TelegramClient
from flask import Flask
from os import path
import logging
from logging import Logger

from .config import Config, load_config


class App:
    instance = None

    def __init__(self, config: Config | str):
        from .register import register_all

        # Assign config data if instance of Config class else load config from .env file
        self.config = config if isinstance(config, Config) else load_config(path.join('../', config))

        # Initializing Telegram client. You can look API_ID and API_HASH on https://my.telegram.org/apps
        self.tgclient: TelegramClient = TelegramClient(
            session='../temp/session.session',
            api_id=self.config.tg_bot.api_id,
            api_hash=self.config.tg_bot.api_hash,
        )
        self.httpserver: Flask = Flask(__name__)
        # Register all controllers and handlers
        register_all(self)

        # Setup logger
        self.logger: Logger = logging.getLogger(__name__)
        logging.basicConfig(
            filename='../temp/logs.log',
            level=logging.INFO,
            format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
        )

    async def start(self):
        try:
            # Connecting to Telegram server and starting http server
            await self.tgclient.connect()
            self.httpserver.run(
                host=self.config.httpserver.host,
                port=self.config.httpserver.port,
            )
        finally:
            # Disconnecting from telegram server
            await self.tgclient.disconnect()
            self.logger.error('Application stopped!')


# Singleton pattern implementation
def get_app(config: Config | str | None = None) -> App:
    if not App.instance:
        App.instance = App(config)
    return App.instance
