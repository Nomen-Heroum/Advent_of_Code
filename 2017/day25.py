import src
from collections import defaultdict

BLUEPRINTS = src.read('\n\n')


def build_turing_machine(blueprints):
    instructions = {}
    for s in blueprints[1:]:
        state, _0, val1, dir1, st1, _1, val2, dir2, st2 = [line.split()[-1][:-1] for line in s.splitlines()]
        instructions[state] = ((val1, dir1, st1), (val2, dir2, st2))

    info = blueprints[0].split()
    state = info[3][0]
    steps = int(info[-2])
    position = 0
    tape = defaultdict(int)
    print("Turing machine built. Checking...\r", end='')
    for _ in range(steps):
        value, direction, state = instructions[state][tape[position]]
        tape[position] = int(value)
        position += 1 if direction == 'right' else -1
    return sum(tape.values())


def main(blueprints=BLUEPRINTS):
    print("Part One:")
    ans1 = build_turing_machine(blueprints)  # 4225
    print(f"The diagnostic checksum is {ans1}.")
    src.clip(ans1)


if __name__ == '__main__':
    main()
