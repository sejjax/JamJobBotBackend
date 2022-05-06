from pyrogram import Client
from pyrogram.errors import AuthKeyUnregistered


async def is_user_auth(client: Client) -> bool:
    try:
        await client.get_me()
        return True
    except AuthKeyUnregistered:
        return False
