import pytest
from seasons import get_age_in_minutes
from datetime import date

def test_birthday_in_future():
    with pytest.raises(SystemExit):
        get_age_in_minutes("2050-01-01")

def test_leap_year():
    result = get_age_in_minutes("2000-02-29")
    assert result is not None
    result = get_age_in_minutes("2016-02-29")
    assert result is not None

def test_today_is_birthday():
    today = str(date.today())
    result = get_age_in_minutes(today)
    assert result == "Zero minutes"
