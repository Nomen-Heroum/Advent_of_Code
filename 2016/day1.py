import src

INSTRUCTIONS = src.read(split=', ')


def find_distance(instructions,  version=1):
    direction = 1j
    place = 0
    visited = {0}
    for instr in instructions:
        if instr[0] == 'L':
            direction *= 1j
        else:
            direction *= -1j
        for _ in range(int(instr[1:])):
            place += direction
            if version > 1 and place in visited:
                return int(abs(place.real) + abs(place.imag))
            visited.add(place)
    return int(abs(place.real) + abs(place.imag))


def main(instructions=INSTRUCTIONS):
    print("Part One:")
    ans1 = find_distance(instructions)
    print(f"The Manhattan distance to my destiny is {ans1} blocks.")

    print("\nPart Two:")
    ans2 = find_distance(instructions, version=2)
    print(f"The first location visited twice is {ans2} blocks away.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
