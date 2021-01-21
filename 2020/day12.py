import src
import parse

STRINGS = src.read()
PATTERN = parse.compile('{}{:d}')
INSTRUCTIONS = [PATTERN.parse(s).fixed for s in STRINGS]
DICT = {
    'N': lambda z, rot, num: (z + num*1j, rot),
    'S': lambda z, rot, num: (z - num*1j, rot),
    'E': lambda z, rot, num: (z + num, rot),
    'W': lambda z, rot, num: (z - num, rot),
    'L': lambda z, rot, num: (z, rot * 1j**(num/90)),
    'R': lambda z, rot, num: (z, rot * (-1j)**(num/90)),
    'F': lambda z, rot, num: (z + rot * num, rot)
}
DICT2 = {
    'N': lambda z, wp, num: (z, wp + num*1j),
    'S': lambda z, wp, num: (z, wp - num*1j),
    'E': lambda z, wp, num: (z, wp + num),
    'W': lambda z, wp, num: (z, wp - num),
    'L': lambda z, wp, num: (z, wp * 1j**(num/90)),
    'R': lambda z, wp, num: (z, wp * (-1j)**(num/90)),
    'F': lambda z, wp, num: (z + wp * num, wp)
}


def follow(instructions: list, dictionary: dict):
    if dictionary == DICT:
        pos = (0, 1)  # Position, heading
    elif dictionary == DICT2:
        pos = (0, 10+1j)  # Position, waypoint
    else:
        raise ValueError("No starting value defined for this instruction dictionary.")
    for inst in instructions:
        key, num = inst
        pos = dictionary[key](*pos, num)
    return int(abs(pos[0].real) + abs(pos[0].imag))


def main(instructions=None):
    instructions = instructions or INSTRUCTIONS

    print("Part One:")
    endpos = follow(instructions, DICT)  # 445
    print(f"The final Manhattan distance from the start is {endpos}.")

    print("\nPart Two:")
    endpos2 = follow(instructions, DICT2)  # 42495
    print(f"The final Manhattan distance is now {endpos2}.")
    src.clip(endpos2)


if __name__ == '__main__':
    main()
