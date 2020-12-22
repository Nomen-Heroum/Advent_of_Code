import src

STRING = src.read(1)[0]


def count_floors(string=STRING):
    floor = 0
    entered_basement = False
    first_basement = "NaN"
    for i, char in enumerate(string):
        assert char in ['(', ')'], "Unexpected character encountered."
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if (not entered_basement) and floor < 0:
            entered_basement = True
            first_basement = i + 1
    print(f"Santa needs to go to floor {floor}.\n"
          f"He first enters the basement on instruction {first_basement} of {len(string)}.")
    return floor, first_basement


src.copy(count_floors())
