import string


def get_min_sq_feet_for_present(dimensions):
    sides = map(int, string.split(dimensions, 'x'))
    side1 = sides[0] * sides[1]
    side2 = sides[1] * sides[2]
    side3 = sides[0] * sides[2]

    return min([side1, side2, side3]) + 2 * (side1 + side2 + side3)

def get_min_sq_feet(presents):
    if type(presents) == str:
        presents = string.split(presents, '\n')
    total = 0;

    for present in presents:
        total += get_min_sq_feet_for_present(present)

    return total
