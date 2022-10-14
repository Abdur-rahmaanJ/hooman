import pytest
from hooman import formula


@pytest.mark.parametrize("val, start, end, realstart, realend, expected", [
	(50, 0, 100, 0, 10, 5), 
	(0, 0, 100, 0, 10, 0), 
	(100, 0, 100, 0, 10, 10), 
	(100, 0, 100, 0, 100, 100), # as is
	(0, 0, 100, 0, 100, 0), # as is
	(59, 0, 100, 0, 100, 59), # as is
	(-1, 0, 100, 0, 100, 0), # less
	(101, 0, 100, 0, 100, 100), # greater than
	])
def test_constrain(val, start, end, realstart, realend, expected):
    assert formula.constrain(val, start, end, realstart, realend) == expected