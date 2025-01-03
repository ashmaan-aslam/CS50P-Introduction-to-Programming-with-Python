from um import count

def test_caps():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um") == 1

def test_punc():
    assert count("um?") == 1
    assert count("um.") == 1
    assert count("um!") == 1

def test_um():
    assert count("yum") == 0
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1
