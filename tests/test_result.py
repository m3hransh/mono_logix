import pytest

def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
