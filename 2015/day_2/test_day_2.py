from problem1 import get_min_sq_feet
from input import INPUT

def test_get_min_sq_feet():
    # input: lxwxh
    assert get_min_sq_feet(['2x3x4']) == 58
    assert get_min_sq_feet(['1x1x10']) == 43
    assert get_min_sq_feet(INPUT) == 1598415
