from enum import Enum
from jamjobbotbackend.services.extract import get_value_by_key_regexp_matching


def test_get_value_by_key_regexp_matching():
    class Color(Enum):
        RED = 0
        GREEN = 1
        BLUE = 2

    class Some(Enum):
        NUMBER = 3

    testRegexpMap = {
        'red': Color.RED,
        'green': Color.GREEN,
        'blue': Color.BLUE,
        '[1-9]{2}': Some.NUMBER
    }
    assert get_value_by_key_regexp_matching(testRegexpMap, 'this is string have a red color ') is Color.RED
    assert get_value_by_key_regexp_matching(testRegexpMap, 'r') is None
    assert get_value_by_key_regexp_matching(testRegexpMap, 'green coper') is Color.GREEN
    assert get_value_by_key_regexp_matching(testRegexpMap, 'blue color') is Color.BLUE
    assert get_value_by_key_regexp_matching(testRegexpMap, 'yop color') is None
    assert get_value_by_key_regexp_matching(testRegexpMap, 'g color') is None
    assert get_value_by_key_regexp_matching(testRegexpMap, 'clock 11') is Some.NUMBER
    assert get_value_by_key_regexp_matching(testRegexpMap, '12 tik') is Some.NUMBER
    assert get_value_by_key_regexp_matching(testRegexpMap, '12tik') is Some.NUMBER
