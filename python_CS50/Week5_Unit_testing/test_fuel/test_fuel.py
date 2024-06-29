from fuel import convert
from fuel import gauge
import pytest


def test_convert_3d4():
    assert convert("3/4") == 75


def test_convert_1d4():
    assert convert("1/4") == 25


def test_convert_4d4():
    assert convert("4/4") == 100


def test_convert_0d4():
    assert convert("0/4") == 0


def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_convert_string_devision():
    with pytest.raises(ValueError):
        convert("three/four")


def test_convert_1pt5d3():
    with pytest.raises(ValueError):
        convert("1.5/3")


def test_gauge_100():
    assert gauge(100) == "F"


def test_gauge_99():
    assert gauge(99) == "F"


def test_gauge_0():
    assert gauge(0) == "E"


def test_gauge_1():
    assert gauge(1) == "E"


def test_gauge_50():
    assert gauge(50) == "50%"
