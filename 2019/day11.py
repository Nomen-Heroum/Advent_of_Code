import src
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

INTCODE = src.read(',', ints=True)


def paint_hull(cpu, version=1):
    painted = defaultdict(int)
    painted[0] = 0 if version == 1 else 1
    position = 0
    direction = -1j
    running = True
    while running:
        cpu.input.append(painted[position])
        colour, turn = cpu.execute()
        painted[position] = colour
        direction *= 1j if turn else -1j
        position += direction
        running = cpu.running

    # Make a plot
    white_x = [int(z.real) for z in painted if painted[z] == 1]
    white_y = [int(z.imag) for z in painted if painted[z] == 1]
    min_x, max_x = min(white_x), max(white_x)
    min_y, max_y = min(white_y), max(white_y)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    array = np.zeros((height, width), int)
    for x, y in zip(white_x, white_y):
        array[y-min_y, x-min_x] = 1
    plt.figure()
    plt.imshow(array, cmap='gray', extent=[min_x, max_x, max_y, min_y])
    if version == 1:
        return len(painted)


def main(intcode=INTCODE):
    cpu = src.IntCodeCPU(intcode)
    print("Part One:")
    ans1 = paint_hull(cpu)  # 1964
    print(f"The robot paints {ans1} panels at least once.")

    print("\nPart Two:")
    paint_hull(cpu, version=2)  # FKEKCFRK
    print(f"Plotted the registration identifier.")


if __name__ == '__main__':
    main()
