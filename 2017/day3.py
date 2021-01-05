import src
import math

SQUARE = 312051


def count_steps(square):
    root = math.sqrt(square)
    layer = math.ceil(root) // 2
    extra = (square - (2 * layer - 1)**2) % (2 * layer)
    return layer + abs(layer - extra)


def build_grid(square):
    filled = {0: 1}
    current = 0
    direction = 1
    while True:
        current += direction
        if current + direction * 1j not in filled:
            direction *= 1j
        fill = sum(v for k, v in filled.items() if abs(k - current) < 2)
        if fill > square:
            return fill
        filled[current] = fill


def main(square=SQUARE):
    print("Part One:")
    ans1 = count_steps(square)  # 430
    print(f"{ans1} steps are needed to get the data from square {square}.")

    print("\nPart Two:")
    ans2 = build_grid(square)  # 312453
    print(f"The first value in the grid larger than {square} is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
