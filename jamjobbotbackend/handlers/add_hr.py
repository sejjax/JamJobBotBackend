from pyrogram import Client, filters
from pyrogram.types import Message

from jamjobbotbackend.services.hr import create_hr_unique
from jamjobbotbackend.filters.hr import hr_filter
from jamjobbotbackend.filters.new_chat import new_chat_filter


def register_add_hr_handler(client: Client):
    @client.on_message(filters.private & hr_filter & new_chat_filter)
    async def add_hr_handler(_, message: Message):
        hr = create_hr_unique(
            telegram_name=message.from_user.first_name,
            telegram_chat_id=message.from_user.id,
            username=message.from_user.username,
        )
        print(hr.telegram_name)
        await client.send_message('sejjax', f'Добавлен новый HR - {hr.username}')
