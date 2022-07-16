from fuel import convert, gauge
import pytest

def main():
    test_value()
    test_zero()
    test_output()

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('2/0')

def test_value():
    with pytest.raises(ValueError):
        convert('a/b')

def test_output():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

if __name__ == "__main__":
    main()
