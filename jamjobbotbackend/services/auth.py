from typing import Optional
from pyrogram import Client
from pyrogram.types.user_and_chats.user import User

sent_codes = {}


# FIXME: This is service can authorize 1 user at the same time

# Send verification code by Telegram
async def send_code(client: Client, phone: str):
    phone = phone.strip()
    sent_code = await client.send_code(phone)
    sent_codes[phone] = sent_code


# Sign In to Telegram account
async def sign_in(client: Client, phone, code: str, password: Optional[str] = None) -> Optional[bool]:
    try:
        sent_codes[phone]
    except:
        return None
    phone_code_hash = sent_codes[phone].phone_code_hash
    return await client.sign_in(
        phone_number=phone,
        phone_code=code,
        phone_code_hash=phone_code_hash
    )


# Sign Out from Telegram account
async def sign_out(client: Client):
    await client.log_out()
