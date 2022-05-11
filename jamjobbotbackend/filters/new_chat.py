from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client


def new_chat_filter_callable(client: Client, message: Message):
    messages = []
    async for message in client.search_messages(message.chat.id, query="", limit=2):
        messages.append(message)
    return len(messages) <= 1


new_chat_filter = filters.create(new_chat_filter_callable)
