import src
import parse

STRINGS = src.read()
INSTRUCTIONS = list(parse.parse('{}{:d}', s) for s in STRINGS)
DIR = ['N', 'E', 'S', 'W']
DICT = {
    'N': lambda x, y, rot, num: (x, y + num, rot),
    'S': lambda x, y, rot, num: (x, y - num, rot),
    'E': lambda x, y, rot, num: (x + num, y, rot),
    'W': lambda x, y, rot, num: (x - num, y, rot),
    'L': lambda x, y, rot, num: (x, y, DIR[(DIR.index(rot) - num//90) % 4]),
    'R': lambda x, y, rot, num: (x, y, DIR[(DIR.index(rot) + num//90) % 4]),
    'F': lambda x, y, rot, num: DICT[rot](x, y, rot, num)
}
DICT2 = {
    'N': lambda x, y, a, b, num: (x, y, a, b + num),
    'S': lambda x, y, a, b, num: (x, y, a, b - num),
    'E': lambda x, y, a, b, num: (x, y, a + num, b),
    'W': lambda x, y, a, b, num: (x, y, a - num, b),
    'L': lambda x, y, a, b, num: (x, y, *src.repeat(lambda a_b: (-a_b[1], a_b[0]), (a, b), num//90)),
    'R': lambda x, y, a, b, num: (x, y, *src.repeat(lambda a_b: (a_b[1], -a_b[0]), (a, b), num//90)),
    'F': lambda x, y, a, b, num: (x + num*a, y + num*b, a, b)
}


def follow(instructions: list, dictionary: dict):
    if dictionary == DICT:
        pos = (0, 0, 'E')
    elif dictionary == DICT2:
        pos = (0, 0, 10, 1)
    else:
        raise ValueError("No starting value defined for this instruction dictionary.")
    for inst in instructions:
        key, num = inst
        pos = dictionary[key](*pos, num)
    return abs(pos[0]) + abs(pos[1])


def main(instructions=None):
    instructions = instructions or INSTRUCTIONS

    print("Part One:")
    endpos = follow(instructions, DICT)
    print(f"The final Manhattan distance from the star is {endpos}.")

    print("\nPart Two:")
    endpos2 = follow(instructions, DICT2)
    print(f"The final Manhattan distance is now {endpos2}.")
    src.clip(endpos2)


if __name__ == '__main__':
    main()
