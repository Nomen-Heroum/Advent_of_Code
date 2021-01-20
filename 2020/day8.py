import src

STRINGS = src.read()


def find_loop(strings, change=None):
    past_instr = []
    i = 0
    acc = 0
    while (i not in past_instr) and (i in range(len(strings))):
        past_instr.append(i)
        ins, num = strings[i].split()

        if i == change:
            if ins == 'nop':
                ins = 'jmp'
            elif ins == 'jmp':
                ins = 'nop'

        if ins == 'jmp':
            i += int(num)
            continue
        elif ins == 'acc':
            acc += int(num)
        i += 1
    return acc, i


def find_fix(strings):
    n = len(strings)
    for c in range(n):
        acc, i = find_loop(strings, change=c)
        if i == n:
            return acc
    return None


def main(strings=STRINGS):
    print("Part One:")
    value = find_loop(strings)[0]
    print(f"The accumulator has value {value} before the program loops.")

    print("\nPart Two:")
    end_value = find_fix(strings)
    print(f"The program finishes successfully with acc={end_value}.")
    src.clip(end_value)


if __name__ == '__main__':
    main()
