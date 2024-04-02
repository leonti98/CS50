from plates import is_valid

def test_valid_CS50():
    assert is_valid("CS50") == True


def test_valid_CS05():
    assert is_valid("CS05") == False


def test_valid_CS50P():
    assert is_valid("CS50P") == False


def test_valid_dot():
    assert is_valid("PI3.14") == False


def test_valid_H():
    assert is_valid("H") == False


def test_valid_OUTATIME():
    assert is_valid("OUTATIME") == False


def test_valid_50():
    assert is_valid("50") == False
