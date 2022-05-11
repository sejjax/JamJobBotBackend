from quart import Quart
from pyrogram import Client

from jamjobbotbackend.controllers import register_auth_controller
from jamjobbotbackend.handlers import register_add_hr_handler


# Register all http controllers and telegram bot handlers
def register(client: Client, app: Quart):
    # register all http controllers
    register_auth_controller(client, app)
    # register all Telegram handlers
    register_add_hr_handler(client)
