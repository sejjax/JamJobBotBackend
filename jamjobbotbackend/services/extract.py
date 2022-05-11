from typing import Optional
from enum import Enum
from dataclasses import dataclass
import datetime
import re

from jamjobbotbackend.models import MeetingServiceType


class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class DayShift(Enum):
    TODAY = 0
    TOMORROW = 1
    DAY_AFTER_TOMORROW = 2


@dataclass
class DateTimeMarkers:
    year: Optional[int]
    time: Optional[datetime.time]
    day: Optional[WeekDay]
    month: Optional[Month]
    day_shift: Optional[DayShift]


def extract_time():
    regexp = r'([0-1]?[0-9]|2[0-3]):[0-5][0-9]'


def extract_date():
    pass


def extract_weekday():
    pass


def extract_day_shift():
    pass


def extract_month():
    pass


def extract_datetime_markers(text: str) -> DateTimeMarkers:
    dayShiftRegexpMap = {
        'сегодня': DayShift.TODAY,
        'завтра': DayShift.TOMORROW,
        'послезавтра': DayShift.DAY_AFTER_TOMORROW
    }

    weekDayRegexpMap = {
        'понедельник|пн': WeekDay.MONDAY,
        'вторник|вт': WeekDay.TUESDAY,
        'сред|ср': WeekDay.WEDNESDAY,
        'четверг|чт': WeekDay.THURSDAY,
        'пятниц|пт': WeekDay.FRIDAY,
        'субот|сб': WeekDay.SATURDAY,
        'воскресен|вс': WeekDay.SUNDAY,
    }

    monthRegexpMap = {
        'январь': Month.JANUARY,
        'февраль': Month.FEBRUARY,
        'март': Month.MARCH,
        'апрель': Month.APRIL,
        'май': Month.MAY,
        'июнь': Month.JUNE,
        'июль': Month.JULY,
        'август': Month.AUGUST,
        'сентябрь': Month.SEPTEMBER,
        'октябрь': Month.OCTOBER,
        'ноябрь': Month.NOVEMBER,
        'декабрь': Month.DECEMBER,
    }


def normalize_datetime_markers(markers: DateTimeMarkers, current_datetime: datetime.datetime) -> datetime.datetime:
    pass


def extract_interview_link(text: str) -> Optional[tuple[str, MeetingServiceType]]:
    url_regexp = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][' \
                 r'a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,' \
                 r'}|www\.[a-zA-Z0-9]+\.[^\s]{2,}) '
    match = re.match(url_regexp, text)
    if match is None:
        return None
