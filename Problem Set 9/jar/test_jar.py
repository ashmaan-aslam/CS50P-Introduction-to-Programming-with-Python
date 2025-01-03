import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    jar = Jar(10)
    assert jar.capacity == 10

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)

def test_capacity():
    jar = Jar(8)
    assert jar.capacity == 8

def test_size():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5
