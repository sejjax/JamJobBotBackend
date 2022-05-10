<<<<<<< Updated upstream
def adding_hr_handler(client, message):
    pass
=======
from pyrogram import Client
from jamjobbotbackend.filters.hr_filter import hr_filter
from pyrogram.types import Message


def register_adding_hr_handler(client: Client):
    async def adding_hr_handler(message: Message):
        await client.send_message('sejjax', message.text)
    return adding_hr_handler
>>>>>>> Stashed changes
