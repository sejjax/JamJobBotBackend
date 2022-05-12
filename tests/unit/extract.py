import pytest

from jamjobbotbackend.services.extract import extract_time, extract_weekday,  WeekDay


@pytest.mark.parametrize('string, expected_result', [
    ('We can call at 05:10', (5, 10)),
    ('20:30', (20, 30)),
    ('1:00', (1, 0)),
    ('23:59', (23, 59)),
    ('24:30', None),
    ('100:30', None),
    ('THis is just a string', None),
    ('10:20 16:13: 17:11', (17, 11)),
    ('11:90', None),
    ('10:20:09', None),
])
def test_extract_time(string, expected_result):
    time = extract_time(string)
    if expected_result is None:
        assert time == expected_result
        return
    assert time.hour == expected_result[0] and time.minute == expected_result[1]


@pytest.mark.parametrize('string, expected_result', [
    ('давай в понедельник', WeekDay.MONDAY),
    ('МОЖЕТ в Понедельник?', WeekDay.MONDAY),
    ('В ПОНЕДЕЛЬНИК?', WeekDay.MONDAY),
    ('назначила на следущий пн', WeekDay.MONDAY),
    ('а в среду?', WeekDay.WEDNESDAY),
    ('а в чт?', WeekDay.THURSDAY),
    ('думаю в ЧЕТВЕРг...', WeekDay.THURSDAY),
    ('в пятницу - ок', WeekDay.FRIDAY),
    ('Вторник. Давай', WeekDay.TUESDAY),
    ('Ненадо в вс', WeekDay.SUNDAY),
    ('воскресенье и птицы', WeekDay.SUNDAY),
    ('субботу и птицы', WeekDay.SATURDAY),
])
def test_extract_weekday(string, expected_result):
    assert extract_weekday(string) == expected_result

# TODO: Write tests for month extractor and day_shift extractor
# TODO: Write tests for interview link extractor
