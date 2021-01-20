import src
import parse

PARTS = src.read('\n\n\n\n')
SAMPLES = PARTS[0].split('\n\n')
INSTR_PATTERN = parse.compile('{:d} {:d} {:d} {:d}')
INSTRUCTIONS = [INSTR_PATTERN.parse(line).fixed for line in PARTS[1].splitlines()]
OPCODES = {
    'addr': lambda reg, a, b: reg[a] + reg[b],
    'addi': lambda reg, a, b: reg[a] + b,
    'mulr': lambda reg, a, b: reg[a] * reg[b],
    'muli': lambda reg, a, b: reg[a] * b,
    'banr': lambda reg, a, b: reg[a] & reg[b],
    'bani': lambda reg, a, b: reg[a] & b,
    'borr': lambda reg, a, b: reg[a] | reg[b],
    'bori': lambda reg, a, b: reg[a] | b,
    'setr': lambda reg, a, b: reg[a],
    'seti': lambda reg, a, b: a,
    'gtir': lambda reg, a, b: int(a > reg[b]),
    'gtri': lambda reg, a, b: int(reg[a] > b),
    'gtrr': lambda reg, a, b: int(reg[a] > reg[b]),
    'eqir': lambda reg, a, b: int(a == reg[b]),
    'eqri': lambda reg, a, b: int(reg[a] == b),
    'eqrr': lambda reg, a, b: int(reg[a] == reg[b]),
}


def find_options(samples, opcodes=None, instr_pattern=INSTR_PATTERN):
    opcodes = opcodes or OPCODES

    count = 0  # For the answer to part 1
    options = {i: set(opcodes) for i in range(len(opcodes))}
    reg_pattern = parse.compile('[{:d}, {:d}, {:d}, {:d}]')
    for sample in samples:
        multiplicity = 0
        reg, changed = [r.fixed for r in reg_pattern.findall(sample)]
        instr, a, b, c = instr_pattern.parse(sample.splitlines()[1])
        for code, func in opcodes.items():
            if reg[:c] + (func(reg, a, b),) + reg[c+1:] == changed:
                multiplicity += 1
            else:
                options[instr] -= {code}
        if multiplicity >= 3:
            count += 1
    return count, options


def reduce_options(options: dict):
    certain = {}
    while options:
        for key, val in options.items():
            if len(val) == 1:
                instr = val.pop()
                certain[key] = instr
                for v in options.values():
                    v -= {instr}
                del options[key]
                break
    return certain


def execute(instructions, opcode_ids, opcodes=None):
    opcodes = opcodes or OPCODES

    reg = [0] * 4
    for op_id, a, b, c in instructions:
        code = opcode_ids[op_id]
        reg[c] = opcodes[code](reg, a, b)
    return reg[0]


def main(samples=None, instructions=None):
    samples = samples or SAMPLES
    instructions = instructions or INSTRUCTIONS

    print("Part One:")
    ans1, options = find_options(samples)  # 640
    print(f"{ans1} of the instructions behave like 3+ opcodes.")

    print("\nPart Two:")
    opcode_ids = reduce_options(options)
    ans2 = execute(instructions, opcode_ids)  # 472
    print(f"The final value in register 0 is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
