import pytest

def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0
