from pyrogram import filters
from pyrogram.types import Message

from jamjobbotbackend.services.hr import is_hr_exist, is_text_from_hr


# Filter messages from HR
def hr_filter_callable(_, __, message: Message):
    return is_text_from_hr(message.text) or is_hr_exist(message.from_user.id)


hr_filter = filters.create(hr_filter_callable)

