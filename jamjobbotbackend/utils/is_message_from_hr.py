import re


def is_message_from_hr(text: str) -> bool:
    # Regexp which must hand all messages from HR
    regexp = r'hr|рекрут|подбор|отклик|hh|пизици|работ|компани|ваканси'
    return re.search(regexp, text.lower()) is not None

