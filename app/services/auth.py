from typing import Optional
from telethon import TelegramClient


class AuthService:
    client: TelegramClient
    phone: str

    def __init__(self, client: TelegramClient):
        self.client = client

    async def send_code(self, phone: str):
        self.phone = phone
        await self.client.send_code_request(phone)

    async def sign_in(self, code: str, password: Optional[str] = None):
        await self.client.sign_in(
            phone=self.phone,
            code=code,
            password=password
        )

    async def log_out(self):
        await self.client.log_out()
