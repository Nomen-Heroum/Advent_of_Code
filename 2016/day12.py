import src

STRINGS = src.read()


def run(strings: list, version=1):
    index = 0
    reg = {'a': 0, 'b': 0, 'c': 0 if version == 1 else 1, 'd': 0}
    while True:
        try:
            instr, *value = strings[index].split(' ')
            index += 1
            if instr == 'cpy':
                try:
                    reg[value[1]] = int(value[0])
                except ValueError:
                    reg[value[1]] = reg[value[0]]
            elif instr == 'inc':
                reg[value[0]] += 1
            elif instr == 'dec':
                reg[value[0]] -= 1
            elif instr == 'jnz':
                try:
                    nonzero = reg[value[0]]
                except KeyError:
                    nonzero = int(value[0])
                if nonzero:
                    index += int(value[1]) - 1
        except IndexError:
            return reg['a']


def main(strings=STRINGS):
    print("Part One:")
    ans1 = run(strings)
    print(f"The final value of register b is {ans1}.")

    print("\nPart Two:")
    ans2 = run(strings, version=2)
    print(f"The final value of b is now {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
