from twttr import shorten

def main():
    test_uppercase()
    test_symbols()

def test_numbers():
    assert shorten('12072022') == '12072022'

def test_uppercase():
    assert shorten('BANANA') == 'BNN'
    assert shorten('banana') == 'bnn'
    assert shorten('baNAnA') == 'bNn'

def test_symbols():
    assert shorten('.,?!@#$%') == '.,?!@#$%'

if __name__ == "__main__":
    main()
