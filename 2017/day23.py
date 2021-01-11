import src
from collections import defaultdict
import math

STRINGS = src.read()
INSTRUCTIONS = {
    'set': lambda _x, y: y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
}


def run(strings: list, debug=True):
    reg = defaultdict(int)
    reg['a'] = 0 if debug else 1

    def value(val):
        try:
            return int(val)
        except ValueError:
            return reg[val]

    count = 0
    index = 0
    while True:
        try:
            if strings == STRINGS and not debug and index == 8:
                step = -int(strings[30].split()[-1])
                # h counts how many numbers between b and c with a step of 'step' (17) are compound
                return sum(any(n % i == 0 for i in range(2, math.isqrt(n) + 1))
                           for n in range(reg['b'], reg['c'] + 1, step))

            instr, *xy = strings[index].split()
            if instr == 'jnz':
                if value(xy[0]):
                    index += value(xy[1]) - 1
            else:
                x, y = [value(v) for v in xy]
                reg[xy[0]] = INSTRUCTIONS[instr](x, y)
                if instr == 'mul':
                    count += 1
            index += 1
        except IndexError:
            return count


def main(strings=STRINGS):
    print("Part One:")
    ans1 = run(strings)  # 3025
    print(f"The mul instruction is invoked {ans1} times.")

    print("\nPart Two:")
    ans2 = run(strings, debug=False)  # 915
    print(f"Register h would end up containing {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
