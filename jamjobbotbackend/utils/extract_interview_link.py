from typing import Optional
from enum import Enum
from jamjobbotbackend.models.Meeting import MeetingServiceType
import re

class MeetingServiceTypeRegexp(Enum, MeetingServiceType):
    GOOGLE_MEETS = 'meets.google.com'
    ZOOM = 'zoom.us'
    MICROSOFT_TEAMS = 'teams.microsoft.com'
    SKYPE = 'skype.com'

def extract_interview_link(text: str) -> Optional[tuple[str, MeetingServiceType]]:
    url_regexp = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][' \
                 r'a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,' \
                 r'}|www\.[a-zA-Z0-9]+\.[^\s]{2,}) '
    match = re.match(url_regexp, text)
    if match is None:
        return None

