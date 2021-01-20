import src
from collections import deque

ELVES = 3017957


def lucky_elf(elves, version=1):
    queue = deque(range(1, elves + 1))
    queue.reverse()

    if version == 1:
        while len(queue) > 1:
            queue.rotate()
            queue.pop()
    else:
        half, odd = divmod(elves, 2)
        queue.rotate(half)
        if not odd:
            queue.pop()
        while len(queue) > 1:
            queue.pop()
            queue.rotate()
            queue.pop()

    return queue[0]


def main(elves=ELVES):
    print("Part One:")
    ans1 = lucky_elf(elves)
    print(f"The lucky elf is Elf {ans1}.")

    print("\nPart Two:")
    ans2 = lucky_elf(elves, 2)
    print(f"The lucky elf is now Elf {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
