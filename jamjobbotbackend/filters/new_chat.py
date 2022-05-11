from pyrogram import Client, filters
from pyrogram.types import Message


# Filter if this message from new chat
def new_chat_filter_callable(client: Client, message: Message):
    messages = client.get_messages(message.chat.id)
    return len(list(messages)) <= 0


new_chat_filter = filters.create(new_chat_filter_callable)
