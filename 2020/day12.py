import src  # My utility functions

STRINGS = src.read()
INSTRUCTIONS = [(s[0], int(s[1:])) for s in STRINGS]

DICT = {  # Instructions for Part 1, contains functions (position, heading, number) -> (position, heading)
    'N': lambda z, rot, n: (z + n*1j, rot),
    'S': lambda z, rot, n: (z - n*1j, rot),
    'E': lambda z, rot, n: (z + n, rot),
    'W': lambda z, rot, n: (z - n, rot),
    'L': lambda z, rot, n: (z, rot * 1j**(n/90)),
    'R': lambda z, rot, n: (z, rot * (-1j)**(n/90)),
    'F': lambda z, rot, n: (z + rot * n, rot)
}
DICT2 = {  # Instructions for Part 2, functions (position, waypoint, number) -> (position, waypoint)
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
        state = (0, 1)  # Position, heading
    elif dictionary == DICT2:
        state = (0, 10+1j)  # Position, waypoint
    else:
        raise ValueError("No starting value defined for this instruction dictionary.")

    for key, num in instructions:
        state = dictionary[key](*state, num)
    return int(abs(state[0].real) + abs(state[0].imag))


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
