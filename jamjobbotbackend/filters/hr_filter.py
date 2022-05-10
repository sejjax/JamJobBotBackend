from pyrogram.filters import create
from pyrogram.types import Message
from jamjobbotbackend.utils.is_message_from_hr import is_message_from_hr


def hr_filter_callable(message: Message):
    return is_message_from_hr(message.text)


hr_filter = create(hr_filter_callable)

