import src
import numpy as np
from scipy.ndimage import convolve

STRING = src.read()[0]


def count_safe(string: str, rows: int):
    n = len(string)
    row = np.array([int(c) for c in string.translate(str.maketrans('.^', '01'))])

    safe = n - row.sum()
    kernel = np.array([1, 0, 1])
    for i in range(1, rows):
        row = convolve(row, kernel, mode='constant') % 2
        safe += n - row.sum()
    return safe


def main(string=STRING):
    print("Part One:")
    ans1 = count_safe(string, 40)
    print(f"There are {ans1} safe tiles.")

    print("\nPart Two:")
    ans2 = count_safe(string, 400_000)
    print(f"There are {ans2} safe tiles.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
