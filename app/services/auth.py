from typing import Optional
from telethon import TelegramClient


async def send_code(client: TelegramClient, phone: str):
    await client.send_code_request(phone, force_sms=True)


async def sign_in(client: TelegramClient, code: str, password: Optional[str] = None):
    await client.sign_in(
        code=code,
        password=password
    )


async def sign_out(client: TelegramClient):
    await client.log_out()
