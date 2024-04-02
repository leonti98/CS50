from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5


def test_negative_capacity():
    with pytest.raises(ValueError):
        jar = Jar(-2)


def test_deposit_exceed():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_deposit_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-15)


def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3


def test_withdraw_exceed():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(15)


def test_withdraw_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-15)
