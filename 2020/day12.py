import src
import parse

STRINGS = src.read()
PATTERN = parse.compile('{}{:d}')
INSTRUCTIONS = [PATTERN.parse(s).fixed for s in STRINGS]

DICT = {  # Instruction dictionary for Part 1
    'N': lambda z, rot, n: (z + n*1j, rot),
    'S': lambda z, rot, n: (z - n*1j, rot),
    'E': lambda z, rot, n: (z + n, rot),
    'W': lambda z, rot, n: (z - n, rot),
    'L': lambda z, rot, n: (z, rot * 1j**(n/90)),
    'R': lambda z, rot, n: (z, rot * (-1j)**(n/90)),
    'F': lambda z, rot, n: (z + rot * n, rot)
}
DICT2 = {  # Dictionary for Part 2
    'N': lambda z, wp, n: (z, wp + n*1j),
    'S': lambda z, wp, n: (z, wp - n*1j),
    'E': lambda z, wp, n: (z, wp + n),
    'W': lambda z, wp, n: (z, wp - n),
    'L': lambda z, wp, n: (z, wp * 1j**(n/90)),
    'R': lambda z, wp, n: (z, wp * (-1j)**(n/90)),
    'F': lambda z, wp, n: (z + wp * n, wp)
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
