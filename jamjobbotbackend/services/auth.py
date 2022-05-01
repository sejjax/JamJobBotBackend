from typing import Optional
from telethon import TelegramClient


# Send verification code by Telegram
async def send_code(client: TelegramClient, phone: str):
    await client.send_code_request(phone, force_sms=True)


# Sign In to Telegram account
async def sign_in(client: TelegramClient, code: str, password: Optional[str] = None):
    await client.sign_in(
        code=code,
        password=password
    )


# Sign Out from Telegram account
async def sign_out(client: TelegramClient):
    await client.log_out()
