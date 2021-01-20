import src
from collections import Counter

STRING = src.read()[0]


def visit_amounts(string=STRING):
    x = 0
    y = 0
    visits = Counter({(0, 0): 1})
    for char in string:
        if char == '>':
            x += 1
        elif char == '<':
            x -= 1
        elif char == '^':
            y += 1
        elif char == 'v':
            y -= 1
        else:
            raise ValueError(f"Unexpected character {char} encountered.")

        if not (x, y) in visits:
            visits[(x, y)] = 1
        else:
            visits[(x, y)] += 1
    return visits


def total_houses(string=STRING):
    houses = len(visit_amounts(string))
    print(f"Santa covered {houses} distinct houses in {len(string) + 1} visits.")
    return houses


def total_houses_2(string=STRING):
    santa = string[::2]
    robot = string[1::2]
    santa_round = visit_amounts(santa)
    robot_round = visit_amounts(robot)
    total_round = santa_round + robot_round
    print(f"Santa covered {len(santa_round)} distinct houses in {len(santa) + 1} visits.\n"
          f"Robo-Santa covered {len(robot_round)} distinct houses in {len(robot) + 1} visits.\n"
          f"Together, they covered {len(total_round)} distinct houses.")
    return len(total_round)


src.clip(total_houses())

print("\nPart Two:")
src.clip(total_houses_2())
