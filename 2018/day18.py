import src
import numpy as np
from scipy.ndimage import convolve

STRINGS = src.read()
AREA = np.array([[int(c == '|') + 10 * int(c == '#') for c in s] for s in STRINGS])


def iterate(area, minutes=10):
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    cache = {}

    for i in range(minutes):
        area_bytes = area.tobytes()
        if area_bytes in cache:
            loop_length = i - cache[area_bytes]
            remainder = (minutes - i) % loop_length
            return iterate(area, remainder)
        cache[area_bytes] = i
        sums = convolve(area, kernel, mode='constant', cval=0)
        yards, trees = divmod(sums, 10)
        new_area = area.copy()
        new_area[(area == 0) & (trees >= 3)] = 1  # Turn empty lots into trees
        new_area[(area == 1) & (yards >= 3)] = 10  # Turn trees into lumberyards
        new_area[(area == 10) & ~((trees >= 1) & (yards >= 1))] = 0  # Turn lumberyards into empty lots
        area = new_area.copy()

    return (area == 1).sum() * (area == 10).sum()


def main(area=AREA):
    print("Part One:")
    ans1 = iterate(area.copy())  # 519478
    print(f"The resource value after 10 minutes is {ans1}.")

    print("\nPart Two:")
    ans2 = iterate(area.copy(), 1000_000_000)  # 210824
    print(f"The resource value after 1,000,000,000 minutes is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
