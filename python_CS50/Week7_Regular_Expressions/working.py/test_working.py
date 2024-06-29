from working import convert
import pytest


def test_convert_default():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_convert_no_zero():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_convert_start_no_minutes():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_convert_no_minutes():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_convert_no_24_to_00():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_convert_exceed_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_convert_exceed_empty():
    with pytest.raises(ValueError):
        convert("")


def test_convert_exceed_cat():
    with pytest.raises(ValueError):
        convert("cat")


def test_convert_P_not_PM():
    with pytest.raises(ValueError):
        convert("9 AM - 5 P")


def test_convert_exceed_hour():
    with pytest.raises(ValueError):
        convert("24 AM - 24 PM")


def test_convert_exceed_hour2():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_convert_exceed_hour1():
    with pytest.raises(ValueError):
        convert("24 AM - 12 PM")


def test_convert_exceed_no_end():
    with pytest.raises(ValueError):
        convert("24 AM")
