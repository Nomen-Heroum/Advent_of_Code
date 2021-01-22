import src  # My utility functions
from collections import deque

STEP_SIZE = 335


def spin(step_size, count=2017):
    buffer = deque([0])
    for i in range(1, count + 1):
        buffer.rotate(-step_size)
        buffer.append(i)
    return buffer[0]


def after_zero(step_size, count=50_000_000):
    after = 0
    current = 0
    for i in range(1, count + 1):
        current = (current + step_size + 1) % i
        if current == 0:
            after = i
    return after


def main(step_size=STEP_SIZE):
    print("Part One:")
    ans1 = spin(step_size)  # 1282
    print(f"The value after 2017 is {ans1}.")

    print("\nPart Two:")
    ans2 = after_zero(step_size)  # 27650600
    print(f"After 50,000,000 is inserted, the value after 0 is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
