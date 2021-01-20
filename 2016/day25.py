import src
import itertools

STRINGS = src.read()


def run(strings: list, a_value: int):
    def reg_int(val):
        try:
            return reg[val]
        except KeyError:
            return int(val)

    index = 0
    reg = {'a': a_value, 'b': 0, 'c': 0, 'd': 0}
    signal = [0, 1]
    while signal[-1] != signal[-2]:
        # Shortcuts
        if strings == STRINGS:
            if index == 1:
                reg['d'] += 15 * 170
                reg['c'] = 0
                reg['b'] = 0
                index = 8
                continue
            elif index == 9:
                half, remainder = divmod(reg['a'], 2)
                reg['a'] = half
                signal.append(remainder)
                index = 28
                continue
            elif index == 29:
                return True

        instr, *value = strings[index].split(' ')

        if instr == 'cpy':
            reg[value[1]] = reg_int(value[0])
        elif instr == 'inc':
            reg[value[0]] += 1
        elif instr == 'dec':
            reg[value[0]] -= 1
        elif instr == 'jnz':
            nonzero = reg_int(value[0])
            if nonzero:
                index += reg_int(value[1]) - 1
        index += 1
    return False


def find_a(strings: list):
    for a in itertools.count(1):
        if run(strings, a):
            return a


def main(strings=STRINGS):
    print("Part One:")
    ans1 = find_a(strings)  # 180
    print(f"The lowest value that works for register a is {ans1}.")
    src.clip(ans1)


if __name__ == '__main__':
    main()
