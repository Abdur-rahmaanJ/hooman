import pytest
from hooman import check


@pytest.mark.parametrize("col, expected", [
	(100, True),
	("", False),
	([], False),
	((), False),
	((10, 10, 10), True),
	([10, 10, 10], True),
	((10, 10), False),
	((10), True),
	((10, 10, 10, 10), False),
	([10, 10], False),
	([10], True),
	([10, 10, 10, 10], False),
	(("d",), False),
	(("d", "d", "d"), False),
	(["d"], False),
	(["d", "d", "d"], False),
	])
def test_constrain(col, expected):
    assert check.check_color(col).success == expected