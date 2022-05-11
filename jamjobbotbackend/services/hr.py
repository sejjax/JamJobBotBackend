from jamjobbotbackend.models.HR import HR
from typing import Optional
from typing import Optional


def create_hr_unique(
    telegram_name: str,
    telegram_chat_id: int,
    username: Optional[str] = None,
    company: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None
) -> Optional[HR]:
    # if hr already exist then return None and will not create a hr
    hr = HR.get_or_none(HR.telegram_chat_id == telegram_chat_id)
    if hr is not None:
        return
    # if hr doesn't exist
    hr = HR(
        telegram_name=telegram_name,
        telegram_chat_id=telegram_chat_id,
        phone=phone,
        username=username,
        company=company,
        email=email
    )
    hr.save()
    return hr


def is_hr_exist(telegram_chat_id: int) -> bool:
    hr = HR.select(HR.telegram_chat_id) \
        .where(HR.telegram_chat_id == telegram_chat_id) \
        .get_or_none()
    return hr is not None
