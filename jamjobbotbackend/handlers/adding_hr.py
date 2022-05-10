from pyrogram import Client
from pyrogram.types import Message


async def adding_hr_handler(client: Client, message: Message):
    await client.send_message('sejjax', message.text)

