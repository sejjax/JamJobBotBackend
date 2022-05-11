from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from jamjobbotbackend.filters.hr_filter import hr_filter
from jamjobbotbackend.services.hr import create_hr

def register_adding_hr_handler(client: Client):
    @client.on_message(filters.private & hr_filter)
    async def adding_hr_handler(_, message: Message):
        create_hr(
            telegram_name=message.from_user.first_name,
            telegram_chat_id=message.from_user.id,
        )
        await client.send_message('sejjax', f'Новый hr создан')
