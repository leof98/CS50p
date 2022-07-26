from jar import Jar


def test_init():
    jar = Jar()
    second_jar = Jar(24)
    assert jar.capacity == 12
    assert second_jar.capacity == 24


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(6)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(6)
    assert jar.size == 6
    jar.withdraw(6)
    assert jar.size == 0
    # 26.07
