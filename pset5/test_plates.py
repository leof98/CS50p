from plates import is_valid

def main():
    test_length()
    test_numbers()

def test_length():
    assert is_valid('AAAA222') == False
    assert is_valid('A') == False

def test_numbers():
    assert is_valid('22AAAA') == False
    assert is_valid('A2AAAA') == False
    assert is_valid('AA22AA') == False

def test_punctuation():
    assert is_valid('AA2.34') == False
    assert is_valid('AA2!34') == False
    assert is_valid('AA2 AA') == False

def test_zero():
    assert is_valid('0AAA22') == False
    assert is_valid('0AA22A') == False

if __name__ == "main":
    main()
# 13/07
