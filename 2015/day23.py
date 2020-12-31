import src

STRINGS = src.read(23)


def run(strings: list, version=1):
    index = 0
    reg = {'a': 0 if version == 1 else 1, 'b': 0}
    while True:
        try:
            instr, value = strings[index].split(' ', 1)
            index += 1
            if instr == 'hlf':
                reg[value] //= 2
            elif instr == 'tpl':
                reg[value] *= 3
            elif instr == 'inc':
                reg[value] += 1
            elif instr == 'jmp':
                index += int(value) - 1
            else:
                r, offset = value.split(', ')
                if (instr == 'jie' and reg[r] % 2 == 0) or (instr == 'jio' and reg[r] == 1):
                    index += int(offset) - 1
        except IndexError:
            return reg['b']


def main(strings=STRINGS):
    src.one()
    ans1 = run(strings)
    print(f"The final value of register b is {ans1}.")

    src.two()
    ans2 = run(strings, version=2)
    print(f"The final value of b is now {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()