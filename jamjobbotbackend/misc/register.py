from jamjobbotbackend.controllers import register_auth_controller
from telethon import TelegramClient
from quart import Quart


# Register all http controllers and telegram bot handlers
def register(client: TelegramClient, app: Quart):
    # register all http controllers
    register_auth_controller(client, app)
