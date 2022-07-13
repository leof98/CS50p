from bank import value

def main():
    test_hello()

def test_hello():
    assert value('hello') == 0
    assert value('hello you') == 0
    assert value('Hello you') == 0


def test_h():
    assert value('h') == 20
    assert value('hahahaha')

def test_else():
    assert value('abcdef') == 100

if __name__ == "main":
    main()
# 12/07
