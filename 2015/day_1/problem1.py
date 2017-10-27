def get_floor(steps):
    cur_floor = 0

    for x in steps:
        if x == '(':
            cur_floor += 1
        else:
            cur_floor -= 1

    return cur_floor

def get_basement_index(steps):
    cur_floor = 0

    for index, step in enumerate(steps):
        cur_floor +=  1 if step == '(' else -1;
        if (cur_floor == -1):
            return index + 1;
