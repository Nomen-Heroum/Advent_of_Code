import src
import numpy as np

NUMBERS = np.array([[int(n) for n in s.split()] for s in src.read(3)])


def count_triangles(numbers: np.ndarray, version=1):
    count = 0
    if version > 1:
        numbers = numbers.T.reshape((-1, 3))
    for triplet in numbers:
        sort = sorted(triplet)
        if sum(sort[:2]) > sort[2]:
            count += 1
    return count


def main(numbers=None):
    numbers = numbers or NUMBERS

    src.one()
    ans1 = count_triangles(numbers)
    print(f"There are {ans1} valid triangles.")

    src.two()
    ans2 = count_triangles(numbers, version=2)
    print(f"Vertically, there are {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
