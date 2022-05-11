#!/usr/bin/python3
import asyncio
import logging

import hypercorn.asyncio
from quart import Quart
from pyrogram import Client

from jamjobbotbackend.misc.config import get_config
from jamjobbotbackend.misc.register import register

config = get_config('.env')

app = Quart(__name__)
logger = logging.getLogger(__name__)
client = Client(
    'JamJobBot',
    api_id=config.tg_bot.api_id,
    api_hash=config.tg_bot.api_hash,
    workdir='temp/'
)
logging.basicConfig(
    filename='temp/app.log',
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)
register(client, app)


@app.before_serving
async def startup():
    logger.info('Application starting')
    await client.start()


@app.after_serving
async def cleanup():
    await client.stop()
    logger.error('Application stopped')


hypercorn_config = hypercorn.Config()
hypercorn_config.bind = [f'{config.httpserver.host}:{config.httpserver.port}']


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(hypercorn.asyncio.serve(app, hypercorn_config))
    except (SystemExit, KeyboardInterrupt):
        logger.error('Application stopped')
