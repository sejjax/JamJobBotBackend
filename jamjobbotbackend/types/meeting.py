from enum import Enum


class MeetingType(Enum):
    # Preliminary interview with HR
    HR_INTERVIEW = 0
    # SoftSkills oriented interview
    SOFTSKILLS_INTERVIEW = 1
    # HardSkills oriented interview
    TECH_INTERVIEW = 2
    # SoftSkills + HardSkills oriented interview
    INTERVIEW = 3


# Enum which define meeting service
class MeetingServiceType(Enum):
    # Default calling via phone (not service)
    PHONE_CALLING = 1
    TELEGRAM = 2
    GOOGLE_MEETS = 3
    ZOOM = 4
    MICROSOFT_TEAMS = 5
    SKYPE = 6
    VKCalling = 7
    SBER_JAZZ = 8
    OTHER = 9
