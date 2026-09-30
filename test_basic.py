from basic import add, multiply

def test_add():
    assert add(2, 5) == 7

def test_multiply():
    assert multiply(2, 4) == 8

def test_divide():
    assert divide(16, 4) == 4