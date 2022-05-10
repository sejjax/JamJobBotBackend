from jamjobbotbackend.controllers import register_auth_controller
from jamjobbotbackend.handlers.adding_hr import adding_hr_handler
from pyrogram import Client
from pyrogram.handlers.message_handler import MessageHandler
from quart import Quart


# Register all http controllers and telegram bot handlers
def register(client: Client, app: Quart):
    # register all http controllers
    register_auth_controller(client, app)
    # register all Telegram handlers
    client.add_handler(MessageHandler(adding_hr_handler))
