import pytest
from fuel import convert, gauge

def test_convert():
    # Test valid fractions
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25

    # Test edge cases
    assert convert("0/1") == 0
    assert convert("1/1") == 100

    # Test invalid fractions
    with pytest.raises(ValueError):
        convert("5/4")  # Numerator > Denominator

    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Denominator is zero

    with pytest.raises(ValueError):
        convert("one/two")  # Non-integer input


def test_gauge():
    # Test edge cases
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

    # Test mid-range values
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
