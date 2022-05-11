from pyrogram import filters
from pyrogram.types import Message
from jamjobbotbackend.utils.is_message_from_hr import is_message_from_hr


def hr_filter_callable(_, __, message: Message):
    return is_message_from_hr(message.text)


hr_filter = filters.create(hr_filter_callable)

