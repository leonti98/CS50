from numb3rs import validate


def test_validate_ip():
    assert validate("123.123.123.123") == True


def test_validate_255():
    assert validate("255.255.255.255") == True


def test_validate_empty():
    assert validate("") == False


def test_validate_letters():
    assert validate("123.fhg.123.123") == False


def test_validate_more_255():
    assert validate("325.200.100.25") == False


def test_validate_512():
    assert validate("512.512.512.512") == False


def test_validate_more_1000end():
    assert validate("1.2.3.1000") == False


def test_validate_cat():
    assert validate("cat") == False


def test_validate_275():
    assert validate("275.3.6.28") == False


def test_validate_259():
    assert validate("259.259.259.259") == False


def test_validate_middle():
    assert validate("100.500.6.28") == False


def test_validate_middle2():
    assert validate("255.255.259.255") == False
