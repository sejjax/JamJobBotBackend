from typing import Optional
from enum import Enum
from dataclasses import dataclass
import datetime


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
    month: Optional[Month]
    weekday: Optional[WeekDay]
    day_shift: Optional[DayShift]
    time: Optional[datetime.time]
