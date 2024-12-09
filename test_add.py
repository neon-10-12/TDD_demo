def test_add_two_positive_numbers():
    from calculator import add
    assert add(1, 0) == 1

def test_add_two_negative_nubber():
    from calculator import add
    assert add(-1, -2) == -3

def test_add_postive_and_negative_number():
    from calculator import add
    assert add(1, -2) == -1

def test_add_zero():
    from calculator import add
    assert add(1, 0) == 1
    assert add(0, 1) == 1
