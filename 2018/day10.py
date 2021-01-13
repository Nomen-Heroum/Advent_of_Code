import src
import numpy as np
import re
import matplotlib.pyplot as plt
import itertools

STRINGS = src.read()
DATA = np.array([[int(n) for n in re.findall(r'-?\d+', S)] for S in STRINGS])
X, Y, VX, VY = DATA.T
Y *= -1
VY *= -1


def find_message(x, y, vx, vy):
    width = x.max() - x.min()
    for i in itertools.count():
        x_i = x + (i + 1) * vx
        new_width = x_i.max() - x_i.min()
        if new_width > width:
            fig, ax = plt.subplots()
            ax.set_aspect(aspect='equal')
            ax.scatter(x + i * vx, y + i * vy)
            return i
        width = new_width


def animate(x, y, vx, vy, frames=20_000, start=0):
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    scat = ax.scatter(x, y)

    def update(i):
        x_i = x + i * vx
        y_i = y + i * vy
        scat.set_offsets(np.array([x_i, y_i]).T)
        return scat,

    return src.Player(fig, update, interval=100, frames=frames, start=start)


def main():
    ans2 = find_message(X, Y, VX, VY)
    print("Part One:")
    print("Plotted the message in a new window.")  # ERCXLAJL

    print("\nPart Two:")
    print(f"The message would have appeared after {ans2} seconds.")  # 10813
    src.copy(ans2)

    print("\nBonus:")
    print(f"Animating the points of light around {ans2} seconds...")
    return ans2


if __name__ == '__main__':
    message_time = main()
    anim = animate(X + message_time * VX, Y + message_time * VY, VX, VY,
                   frames=np.arange(-5, 5, 0.1), start=-5)
