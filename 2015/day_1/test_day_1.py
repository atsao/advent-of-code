from problem1 import get_floor, get_basement_index
from input import INPUT

def test_get_floor():
    assert get_floor('(())') == 0
    assert get_floor('()()') == 0
    assert get_floor('(((') == 3
    assert get_floor('(()(()(') == 3
    assert get_floor('))(((((') == 3
    assert get_floor('())') == -1
    assert get_floor('))(') == -1
    assert get_floor(')))') == -3
    assert get_floor(')())())') == -3
    assert get_floor(INPUT) == 232

def test_get_basement_index():
    assert get_basement_index(')') == 1
    assert get_basement_index('()())') == 5
    assert get_basement_index(INPUT) == 1783
