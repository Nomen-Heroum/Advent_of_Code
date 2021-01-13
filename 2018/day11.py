import src
import numpy as np
from copy import deepcopy

SERIAL_NUMBER = 8199


def fullest_region(serial_number, size=300):
    power_levels = np.empty((size, size), int)
    for x in range(size):
        for y in range(size):
            power_levels[y, x] = ((x + 11) * (y + 1) + serial_number) * (x + 11)
    power_levels //= 100
    power_levels %= 10
    power_levels -= 5

    coordinate = None
    best_region = 0
    best_size = 0
    best_x = None
    best_y = None
    add = deepcopy(power_levels)
    regions = np.zeros_like(power_levels)
    for i in range(1, size+1):
        end = size + 1 - i
        regions[:end, :end] += add[:end, :end]
        add[:-i, :-i] = add[1:end, 1:end] + power_levels[i:, :-i] + power_levels[:-i, i:]  # Magic :)
        if i == 3:
            y, x = divmod(regions.argmax(), size)
            coordinate = f"{x+1},{y+1}"
        maximum = regions.max()
        if maximum > best_region:
            best_region = maximum
            best_size = i
            best_y, best_x = np.argwhere(regions == maximum)[0]
    return coordinate, f"{best_x+1},{best_y+1},{best_size}"


def main(serial_number=SERIAL_NUMBER):
    ans1, ans2 = fullest_region(serial_number)
    print("Part One:")
    print(f"The X,Y coordinate required is {ans1}.")  # 235,87

    print("\nPart Two:")
    print(f"The best size coordinate is {ans2}.")  # 234,272,18
    src.copy(ans2)


if __name__ == '__main__':
    main()
