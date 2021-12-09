import src  # My utility functions

INSTRUCTIONS = src.read()
DIRECTIONS = {
    "forward": 1,
    "down": 1j,
    "up": -1j
}


def execute(instructions):
    position = 0
    for instr in instructions:
        direction, num = instr.split()
        position += int(num) * DIRECTIONS[direction]
    return int(position.real * position.imag)


def alt_execute(instructions):
    position = 0
    aim = 0j
    for instr in instructions:
        direction, num = instr.split()
        if direction == "forward":
            position += int(num) * (1 + aim)
        else:
            aim += int(num) * DIRECTIONS[direction]
    return int(position.real * position.imag)


def main(instructions=INSTRUCTIONS):
    print("Part One:")
    ans1 = execute(instructions)  # 2147104
    print(f"Multiplying the depth and horizontal position gives {ans1}.")

    print("\nPart Two:")
    ans2 = alt_execute(instructions)  # 2044620088
    print(f"The result changes to {ans2} under the new rules.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
