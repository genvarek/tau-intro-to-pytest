import pytest


def test_one_plus_one():
    assert 1+1 == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert "division by zero" in str(e.value)

products = [
    (2, 3, 6), # positive integers
    (1, 23, 23), # identity
    (0, 1234, 0), # zero
    (1, -1, -1), # positive by negative
    (-2, -2, 4), # negative by negative
    (0.5, 2.0, 1.0) # float
]

@pytest.mark.parametrize("a, b, product", products)
def test_multiplictation(a, b, product):
    assert a * b == product