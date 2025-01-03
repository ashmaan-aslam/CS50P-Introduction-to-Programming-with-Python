from twttr import shorten

def test_str():
    assert shorten("Ashmaan") == "shmn"

def test_number():
    assert shorten("Ashmaan10") == "shmn10"

def test_punc():
    assert shorten("Ashmaan, ashmaan") == "shmn, shmn"
