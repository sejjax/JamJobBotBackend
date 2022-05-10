import re


def is_message_from_hr(text: str) -> bool:
    # Regexp which must hand all messages from HR
    regexp = r'hr|рекрутер|подбор|отклик|hh|пизици|работ|компани|ваканси|компани'
    return re.match(regexp, text.lower()) is not None

