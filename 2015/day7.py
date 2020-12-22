import src

instructions = src.read(7)

OPERATORS = {
    'NOT': lambda x: ~x,
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y
}


def process(input_strings: list, wires: dict):
    """Returns the values that the strings in input_strings represent."""
    output = []
    for item in input_strings:
        if item in wires:
            output.append(wires[item])
        elif item in OPERATORS:
            output.append(OPERATORS[item])
        elif item.isdigit():
            output.append(int(item))
        else:
            raise ValueError("Unknown object in list.")
    return output


def apply(inp: list):
    """Returns the output produced by inp."""
    n = len(inp)
    if n == 1:
        out = inp[0]
    elif n == 2:
        out = inp[0](inp[1])
    elif n == 3:
        out = inp[1](inp[0], inp[2])
    else:
        raise ValueError("List has unexpected length.")
    return out


def main(instr=instructions, part=1):
    wires = {}
    if part == 2:
        wires['b'] = 46065
    while 'a' not in wires:
        for line in instr:
            words = line.split()
            out = words[-1]
            if out in wires:
                continue
            input_strings = words[:-2]
            try:
                input_list = process(input_strings, wires)
            except ValueError:
                continue
            wires[out] = apply(input_list)
    print(f"Final value of wire a is {wires['a']}.")
    src.copy(wires['a'])


if __name__ == '__main__':
    print("Part One:")
    main()
    print("\nPart Two:")
    main(part=2)
