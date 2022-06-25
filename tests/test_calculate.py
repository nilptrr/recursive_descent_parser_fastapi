import pytest

from src.rdp.calculator import calculate


def test_valid_expr():
    assert calculate('+100.1') == 100.1
    assert calculate('-0') == 0
    assert calculate('-7 / 34.2') == -0.205
    assert calculate('- 6 * 2') == -12
    # assert calculate('2. / 1.') == 2                  # not implemented yet
    assert calculate('(2 + 3.1) * 5 / 4') == 6.375
    assert calculate('5 + - 4') == 1


def test_invalid_expr():
    with pytest.raises(TypeError):
        calculate('*1 + 7')
        calculate('4 / 3 +')
