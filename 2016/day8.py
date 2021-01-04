import src
import numpy as np
import re
import matplotlib.pyplot as plt

INSTRUCTIONS = src.read(8)
SCREEN = np.zeros((6, 50), dtype=int)


def follow(instructions, screen):
    for instr in instructions:
        a, b = (int(s) for s in re.findall(r'\d+', instr))
        if 'rect' in instr:
            screen[:b, :a] = 1
        elif 'row' in instr:
            screen[a] = np.concatenate((screen[a, -b:], screen[a, :-b]))
        else:
            screen[:, a] = np.concatenate((screen[-b:, a], screen[:-b, a]))
    plt.imshow(screen)
    return screen.sum()


def main(instructions=INSTRUCTIONS, screen=SCREEN):
    print("Part One:")
    ans1 = follow(instructions, screen)
    print(f"{ans1} lights are on after following the instructions.")
    src.copy(ans1)

    print("\nPart Two:")
    print(f"Plotted the code on the display.")


if __name__ == '__main__':
    main()
