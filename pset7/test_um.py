from um import count

def main():
    test_space()
    test_word()
    test_count()
    test_case()

def test_count():
    assert count('..um..um..um.') == 3

def test_space():
    assert count(' um ') == 1
    assert count('um aaa') == 1
    assert count('um') == 1

def test_word():
    assert count('yummy') == 0

def test_case():
    assert count('UM') == 1
    assert count('Um, a, um') == 2

if __name__ == '__main__':
    main()
# 20.07
