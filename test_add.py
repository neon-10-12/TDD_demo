def test_add_two_positive_numbers():
    from calculator import add
    assert add(1, 0) == 1

def test_add_two_negative_nubber():
    from calculator import add
    assert add(-1, -2) == -3