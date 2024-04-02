from seasons import get_difference
import pytest


def test_get_difference_one_year():
    assert (
        get_difference("2022-11-25")
        == "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_get_difference_two_year():
    assert (
        get_difference("2021-11-25")
        == "One million, fifty-one thousand, two hundred minutes"
    )


def test_get_difference_invalid_date():
    with pytest.raises(SystemExit) as excinfo:
        get_difference("")
    assert excinfo.type == SystemExit


def test_get_difference_dots():
    with pytest.raises(SystemExit) as excinfo:
        get_difference("2022.06.22")
    assert excinfo.type == SystemExit


def test_get_difference_slash():
    with pytest.raises(SystemExit) as excinfo:
        get_difference("2022/06/22")
    assert excinfo.type == SystemExit
