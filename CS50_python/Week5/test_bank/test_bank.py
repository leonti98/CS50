from bank import value


def test_value_Hello():
    assert value("Hello") == 0


def test_value_Hello_Newman():
    assert value("Hello, Newman") == 0


def test_value_How_you_doing():
    assert value("How you doing?") == 20


def test_value_Whats_happening():
    assert value("What's happening?") == 100
