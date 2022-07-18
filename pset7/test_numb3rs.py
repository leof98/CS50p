from numb3rs import validate

def main():
    test_number()
    test_lenght()

def test_number():
    assert validate(r'255.1.1.1') == True
    assert validate(r'256.1.1.1') == False
    assert validate(r'1.256.1.1') == False
    assert validate(r'1.1.256.1') == False
    assert validate(r'1.1.1.256') == False
    assert validate(r'-1.1.1.1') == False

def test_lenght():
    assert validate(r'255.255.255.255') == True
    assert validate(r'1') == False
    assert validate(r'1.1.1.1.1') == False
    assert validate(r'1.1.1.1')

if __name__ == '__main__':
    main()
# 18.07
