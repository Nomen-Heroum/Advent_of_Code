import src

STRINGS = src.read()
INSTRUCTIONS = {'U': 1j, 'D': -1j, 'L': -1, 'R': 1}
KEYS = {-1+1j: '1', 1j: '2', 1+1j: '3',
        -1: '4', 0: '5', 1: '6',
        -1-1j: '7', -1j: '8', 1-1j: '9'}

KEYS2 = {2+2j: '1',
         1+1j: '2', 2+1j: '3', 3+1j: '4',
         0: '5', 1: '6', 2: '7', 3: '8', 4: '9',
         1-1j: 'A', 2-1j: 'B', 3-1j: 'C',
         2-2j: 'D'}


def find_code(strings, keys=None, instructions=None):
    keys = keys or KEYS
    instructions = instructions or INSTRUCTIONS

    position = 0
    code = ''
    for s in strings:
        for c in s:
            newpos = position + instructions[c]
            if newpos in keys:
                position = newpos
        code += keys[position]
    return code


def main(strings=STRINGS):
    print("Part One:")
    ans1 = find_code(strings)
    print(f"The bathroom code is {ans1}.")

    print("\nPart Two:")
    ans2 = find_code(strings, keys=KEYS2)
    print(f"It's actually {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
