import src  # My utility functions
from collections import defaultdict, deque

STRINGS = src.read()
INSTRUCTIONS = {
    'set': lambda _x, y: y,
    'add': lambda x, y: x + y,
    'mul': lambda x, y: x * y,
    'mod': lambda x, y: x % y
}


def run(strings: list):
    reg = defaultdict(int)

    def value(val):
        try:
            return int(val)
        except ValueError:
            return reg[val]

    frequency = 0
    index = 0
    while True:
        instr, *xy = strings[index].split()
        index += 1
        if instr == 'snd':
            frequency = value(xy[0])
        elif instr == 'rcv':
            if value(xy[0]):
                return frequency
        elif instr == 'jgz':
            if value(xy[0]) > 0:
                index += value(xy[1]) - 1
        else:
            x, y = [value(v) for v in xy]
            reg[xy[0]] = INSTRUCTIONS[instr](x, y)


def run_parallel(strings: list):
    reg = [defaultdict(int), defaultdict(int)]
    reg[1]['p'] = 1
    p = 0  # Current program ID

    def value(val):
        try:
            return int(val)
        except ValueError:
            return reg[p][val]

    index = [0, 0]
    send_queue = [deque(), deque()]
    waiting = [False, False]
    wait_reg = [None, None]
    result = 0
    while True:
        instr, *xy = strings[index[p]].split()
        if instr == 'snd':
            send_queue[p].append(value(xy[0]))
            result += p
        elif instr == 'rcv':
            try:
                reg[p][xy[0]] = send_queue[p ^ 1].popleft()  # Pop from the other queue
            except IndexError:
                waiting[p] = True
                wait_reg[p] = xy[0]
                p ^= 1  # Switch to the other program
                if waiting[p]:
                    try:
                        reg[p][wait_reg[p]] = send_queue[p ^ 1].popleft()
                    except IndexError:
                        return result
                else:
                    continue
        elif instr == 'jgz':
            if value(xy[0]) > 0:
                index[p] += value(xy[1]) - 1
        else:
            x, y = [value(v) for v in xy]
            reg[p][xy[0]] = INSTRUCTIONS[instr](x, y)
        index[p] += 1


def main(strings=STRINGS):
    print("Part One:")
    ans1 = run(strings)  # 2951
    print(f"The first recovered frequency is {ans1}.")

    print("\nPart Two:")
    ans2 = run_parallel(strings)
    print(f"Program 1 sent a value {ans2} times.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
