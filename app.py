#!/usr/bin/env/python3
# import asyncio
#
# import hypercorn.asyncio
# from quart import Quart
# from telethon import TelegramClient
# from jamjobbotbackend.misc.config import get_config
# from jamjobbotbackend.misc.register import register
# import logging
#
# config = get_config('.env')
# client = TelegramClient(
#     api_id=config.tg_bot.api_id,
#     api_hash=config.tg_bot.api_hash,
#     session='temp/session.session'
# )
# app = Quart(__name__)
# logger = logging.getLogger(__name__)
#
# logging.basicConfig(
#     filename='temp/app.log',
#     level=logging.INFO,
#     format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
# )
# register(client, app)
#
#
# @app.before_serving
# async def startup():
#     logger.info('Application starting')
#     await client.connect()
#     h = client.is_connected()
#     print('...')
#
#
# @app.after_serving
# async def cleanup():
#     logger.error('Application stopped')
#     await client.disconnect()
#
#
# hypercorn_config = hypercorn.Config()
# hypercorn_config.bind = [f'{config.db.host}:{config.db.port}']
#
#
# async def main():
#     await hypercorn.asyncio.serve(app, hypercorn_config)
#
#
# if __name__ == '__main__':
#     try:
#         asyncio.run(main())
#     except (SystemExit, KeyboardInterrupt):
#         logger.error('Application stopped')
print('hello world')
