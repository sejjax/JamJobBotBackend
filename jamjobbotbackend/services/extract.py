from datetime import datetime
from typing import Optional
from enum import Enum
from dataclasses import dataclass
import datetime
import regex

from jamjobbotbackend.types.meeting import MeetingServiceType
from jamjobbotbackend.types.date import DateTimeMarkers, Month, WeekDay, DayShift


# Return dictionary value if that key is matched part of string
def get_value_by_key_regexp_matching(regexpMap: dict, string: str) -> Optional[str]:
    for regexp in regexpMap.keys():
        match = regex.findall(regexp, string)
        if len(match) is 0:
            continue
        return regexpMap[regexp]
    return None


# Extractors
def extract_time(text: str) -> Optional[datetime.time]:
    regexp = r'(?<![\d:\w])[0-9]{1,2}:[0-9]{1,2}(?![\d:\w])'
    match = regex.findall(regexp, text.lower())
    if len(match) is 0:
        return None
    last = match.pop()
    hour, minute = last.split(':')
    hour, minute = int(hour), int(minute)
    if hour > 23 or minute > 59:
        return None
    return datetime.time(hour=hour, minute=minute)


def extract_weekday(string: str) -> Optional[WeekDay]:
    # (?<=\s|^)(пн|понедельник)(?=\s|$\W) can match strict only with spaces around or start or end line
    weekDayRegexpMap = {
        '((?<=\s|^)(пн)(?=\s|$|\W))|понедельник': WeekDay.MONDAY,
        '((?<=\s|^)(вт)(?=\s|$|\W))|вторник': WeekDay.TUESDAY,
        '((?<=\s|^)(ср)(?=\s|$|\W))|сред': WeekDay.WEDNESDAY,
        '((?<=\s|^)(чт)(?=\s|$|\W))|четверг': WeekDay.THURSDAY,
        '((?<=\s|^)(пт)(?=\s|$|\W))|пятниц': WeekDay.FRIDAY,
        '((?<=\s|^)(сб)(?=\s|$|\W))|суббот': WeekDay.SATURDAY,
        '((?<=\s|^)(вс)(?=\s|$|\W))|воскресень': WeekDay.SUNDAY,
    }
    return get_value_by_key_regexp_matching(weekDayRegexpMap, string.lower())


def extract_day_shift(string: str) -> Optional[DayShift]:
    dayShiftRegexpMap = {
        'сегодн': DayShift.TODAY,
        'завтр': DayShift.TOMORROW,
        'послезавтр': DayShift.DAY_AFTER_TOMORROW
    }
    return get_value_by_key_regexp_matching(dayShiftRegexpMap, string)


def extract_month(string: str) -> Optional[Month]:
    monthRegexpMap = {
        '((?<=\s|^)(янв)(?=\s|$|\W))|январь': Month.JANUARY,
        '((?<=\s|^)(фев)(?=\s|$|\W))|февраль': Month.FEBRUARY,
        '((?<=\s|^)(мар)(?=\s|$|\W))|март': Month.MARCH,
        '((?<=\s|^)(апр)(?=\s|$|\W))|апрель': Month.APRIL,
        '((?<=\s|^)(май)(?=\s|$|\W))|май': Month.MAY,
        '((?<=\s|^)(июн)(?=\s|$|\W))|июнь': Month.JUNE,
        '((?<=\s|^)(июл)(?=\s|$|\W))|июль': Month.JULY,
        '((?<=\s|^)(авг)(?=\s|$|\W))|август': Month.AUGUST,
        '((?<=\s|^)(сен)(?=\s|$|\W))|сентябрь': Month.SEPTEMBER,
        '((?<=\s|^)(окт)(?=\s|$|\W))|октябрь': Month.OCTOBER,
        '((?<=\s|^)(ноя)(?=\s|$|\W))|ноябрь': Month.NOVEMBER,
        '((?<=\s|^)(дек)(?=\s|$|\W))|декабрь': Month.DECEMBER,
    }
    return get_value_by_key_regexp_matching(monthRegexpMap, string)


# Safe setters set datetime param.
# If this param greater than max value, then increase most significant param
# Sequence: month <- weekday + day_shift <- time
def set_time_safe(_datetime: datetime.datetime, time: datetime.time):
    MAX_HOUR_MINUTES = 59
    MAX_DAY_HOURS = 23


def set_weekday_safe(_datetime: datetime.datetime, weekday: WeekDay):
    if _datetime.weekday() >= weekday.value:
        return _datetime.replace(
            year=_datetime.year + 1,
            weekday=weekday.value
        )
    return _datetime.replace(
        month=month.value
    )


def set_month_safe(_datetime: datetime.datetime, month: Month):
    if _datetime.month >= month.value:
        return _datetime.replace(
            year=_datetime.year + 1,
            month=month.value
        )
    return _datetime.replace(
        month=month.value
    )


def set_day_shift_safe(_datetime: datetime.datetime, day_shift: DayShift):
    return set_weekday_safe(_datetime, _datetime.day + day_shift.value)


def extract_datetime_markers(string: str) -> DateTimeMarkers:
    day_shift = extract_day_shift(string)
    weekday = extract_weekday(string)
    month = extract_month(string)
    time = extract_time(string)
    return DateTimeMarkers(
        day_shift=day_shift,
        weekday=weekday,
        month=month,
        time=time
    )


def normalize_datetime_markers(markers: DateTimeMarkers, current_datetime: datetime.datetime) -> datetime.datetime:
    current_datetime.replace(
        hour=markers.time.hour,
        minute=markers.time.minute,
        month=markers.month.value,
        day=markers.weekday.value
    )
    return current_datetime


def extract_interview_link(string: str) -> Optional[tuple[str, Optional[MeetingServiceType]]]:
    meetingServiceTypeRegexpMap = {
        'meats.google.com': MeetingServiceType.GOOGLE_MEETS,
        'teams.micosoft.com': MeetingServiceType.MICROSOFT_TEAMS,
        'zoom.us': MeetingServiceType.ZOOM,
        'skype.com': MeetingServiceType.SKYPE,
        'jazz.sber.ru': MeetingServiceType.SBER_JAZZ,
    }
    url_regexp = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][' \
                 r'a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,' \
                 r'}|www\.[a-zA-Z0-9]+\.[^\s]{2,}) '
    match = re.search(url_regexp, string)
    if match is None:
        return None
    last = match[-1]
    service_type = get_value_by_key_regexp_matching(meetingServiceTypeRegexpMap, url_regexp)
    return last, service_type
