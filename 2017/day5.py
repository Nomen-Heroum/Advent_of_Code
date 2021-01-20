import src
from copy import copy

JUMPS = src.read(ints=True)


def count_steps(jumps, version=1):
    index = 0
    steps = 0
    while True:
        try:
            jump = jumps[index]
            jumps[index] += 1 if version == 1 or jump < 3 else -1
            index += jump
            steps += 1
        except IndexError:
            return steps


def main(jumps=None):
    jumps = jumps or JUMPS

    print("Part One:")
    ans1 = count_steps(copy(jumps))  # 381680
    print(f"It takes {ans1} jumps to reach the exit.")

    print("\nPart Two:")
    ans2 = count_steps(copy(jumps), version=2)  # 29717847
    print(f"It now takes {ans2} steps.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
