import src  # My utility functions
import numpy as np

STRINGS = src.read()


def simulate_jellyfish(arr: np.ndarray, steps=100):
    n = len(arr)
    flashes = 0
    step = 0
    while True:
        step += 1
        arr += 1
        flashed = np.full(arr.shape, False)
        to_flash = np.argwhere(arr > 9)
        while to_flash.size > 0:
            flashed = arr > 9
            for x, y in to_flash:
                # Try increasing all neighbours by 1
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if (dx, dy) != (0, 0) and 0 <= x + dx <= n - 1 and 0 <= y + dy <= n - 1:
                            arr[x + dx, y + dy] += 1
            to_flash = np.argwhere((arr > 9) != flashed)

        arr[arr > 9] = 0
        if step <= steps:
            flashes += np.sum(flashed)
        elif np.sum(flashed) == arr.size:
            break

    return flashes, step


def main(strings=STRINGS, steps=100):
    arr = np.genfromtxt(strings, int, delimiter=1)
    ans1, ans2 = simulate_jellyfish(arr, steps)  # 1601, 368
    print("Part One:")
    print(f"After 100 steps there have been {ans1} flashes.")

    print("\nPart Two:")
    print(f"The first step during which all octopuses flash is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
