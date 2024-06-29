import pytest
from credit import validate

def test_short():
    assert validate("123") == False

def test_long():
    assert validate("1234567890123456789") == False

def test_14():
    assert validate("12345678901234") == False

def test_AMEX_1():
    assert validate("378282246310005") == "AMEX"

def test_AMEX_2():
    assert validate("371449635398431") == "AMEX"

def test_MASTERCARD_1():
    assert validate("5555555555554444") == "MASETERCARD"

def test_MASTERCARD_2():
    assert validate("5105105105105100") == "MASETERCARD"

def test_VISA_1():
    assert validate("4111111111111111") == "VISA"

def test_VISA_2():
    assert validate("4012888888881881") == "VISA"
