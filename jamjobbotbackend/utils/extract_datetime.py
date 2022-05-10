import datetime
from enum import Enum
from dataclasses import dataclass
from typing import Optional


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
