import src
import parse
import math

STRINGS = src.read()
POINTER = int(STRINGS[0][-1])
INSTR_PATTERN = parse.compile('{} {:d} {:d} {:d}')
INSTRUCTIONS = [INSTR_PATTERN.parse(line).fixed for line in STRINGS[1:]]
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


def execute(instructions, pointer=POINTER, opcodes=None, version=1):
    opcodes = opcodes or OPCODES

    reg = [0] * 6
    if version > 1:
        reg[0] = 1
    while True:
        try:
            # Shortcut
            if reg[pointer] == 1:  # Return the sum of all divisors of reg[2]
                root = math.isqrt(reg[2])
                divisor_sum = sum(i + reg[2] // i
                                  for i in range(1, root + 1)
                                  if reg[2] % i == 0)
                if root**2 == reg[2]:
                    divisor_sum -= root
                return divisor_sum

            instr, a, b, c = instructions[reg[pointer]]
            reg[c] = opcodes[instr](reg, a, b)
            reg[pointer] += 1
        except IndexError:
            return reg[0]


def main(instructions=None):
    instructions = instructions or INSTRUCTIONS

    print("Part One:")
    ans1 = execute(instructions)  # 1350
    print(f"Register 0 has value {ans1} when the program halts.")

    print("\nPart Two:")
    ans2 = execute(instructions, version=2)  # 15844608
    print(f"The new process halts with value {ans2} in register 0.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
