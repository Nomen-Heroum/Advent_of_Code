import src
from collections import defaultdict
from parse import parse

STRINGS = src.read()


def run(strings):
    reg = defaultdict(int)
    largest = 0
    for s in strings:
        r1, instr, amount, r2, op = parse('{} {} {:d} if {:w}{}', s)
        if eval(str(reg[r2]) + op):
            reg[r1] += amount if instr == 'inc' else -amount
            largest = max(largest, reg[r1])
    return max(reg.values()), largest


def main(strings=STRINGS):
    ans1, ans2 = run(strings)
    print("Part One:")
    print(f"The largest value in any register at the end is {ans1}.")  # 3880

    print("\nPart Two:")
    print(f"The largest value in any register ever is {ans2}.")  # 5035
    src.copy(ans2)


if __name__ == '__main__':
    main()
