#!/usr/bin/env python3

import asyncio
import logging

from jamjobbotbackend.app import get_app

logger = logging.getLogger(__name__)


async def main():
    app = get_app(config='.env')
    logger.info('Application starting')
    await app.start()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Application stopped!")
