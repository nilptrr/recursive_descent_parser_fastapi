import pytest

from src.rdp.calculator import calculate


@pytest.mark.parametrize(
    'expr, result', 
    [
        ('+100.1', 100.1),
        ('-0', 0),
        ('-7 / 34.2', -0.205),
        ('- 6 * 2', -12),
        ('(2 + 3.1) * 5 / 4', 6.375),
        ('5 + - 4', 1),
        # ('2. / 1.', 2)  # not implemented yet
    ]
)
def test_valid_expr(expr, result):
    assert calculate(expr) == result


@pytest.mark.parametrize(
    'expr, expectaion', 
    (
        ['*1 + 7', pytest.raises(TypeError)],
        ['4 / 3 +', pytest.raises(TypeError)]
    )
)
def test_invalid_expr(expr, expectaion):
    with expectaion:
        assert calculate(expr)
        # calculate(expr)
