import src
from collections import defaultdict

STRINGS = src.read()
TOGGLE_DICT = {'inc': 'dec',
               'dec': 'inc',
               'tgl': 'inc',
               'jnz': 'cpy',
               'cpy': 'jnz'}


def run(strings: list, version=1, toggle_dict=None):
    toggle_dict = toggle_dict or TOGGLE_DICT

    def reg_int(val):
        try:
            return reg[val]
        except KeyError:
            return int(val)

    index = 0
    reg = {'a': 7 if version == 1 else 12, 'b': 0, 'c': 0, 'd': 0}
    toggled = defaultdict(bool)
    while True:
        try:
            # Shortcuts
            if strings == STRINGS:
                if index == 4:
                    reg['a'] = reg['b'] * reg['d']
                    reg['c'] = 0
                    reg['d'] = 0
                    index = 10
                    continue
                elif index == 11:
                    reg['c'] = 2 * reg['b']
                    reg['d'] = 0
                    index = 16
                    continue
                elif index == 19:
                    a, b = [int(strings[i].split()[1]) for i in (19, 20)]
                    return reg['a'] + a * b

            instr, *value = strings[index].split(' ')
            if toggled[index]:
                instr = toggle_dict[instr]

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
            elif instr == 'tgl':
                target = index + reg[value[0]]
                toggled[target] = not toggled[target]
            index += 1
        except IndexError:
            return reg['a']


def main(strings=STRINGS):
    print("Part One:")
    ans1 = run(strings)  # 14065
    print(f"The value sent to the safe is {ans1}.")

    print("\nPart Two:")
    ans2 = run(strings, version=2)  # 479010625
    print(f"The final value sent to the safe is now {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
