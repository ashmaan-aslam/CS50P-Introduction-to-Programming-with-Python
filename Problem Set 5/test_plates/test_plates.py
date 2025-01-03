from plates import is_valid

def test_start():
    assert is_valid("cs50") == True
    assert is_valid("c120") == False

def test_max():
    assert is_valid("AAA222") == True
    assert is_valid("AA") == True

    assert is_valid("AAA2223") == False
    assert is_valid("A") == False

def test_middle():
    assert is_valid("BBB233") == True
    assert is_valid("AAA22A") == False

def test_punc():
    assert is_valid("PI3.14") == False

def test_invalid_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("A50") == False
    assert is_valid("AA01") == False
