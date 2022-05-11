from jamjobbotbackend.models.HR import HR
from typing import Optional


def create_hr(
    telegram_name: str,
    telegram_chat_id: int,
    username: Optional[str],
    company: Optional[str],
    email: Optional[str],
    phone: Optional[str]
):
    return HR.create(
        telegram_name=telegram_name,
        phone=phone,
        telegram_chat_id=telegram_chat_id,
        username=username,
        company=company,
        email=email
    )
