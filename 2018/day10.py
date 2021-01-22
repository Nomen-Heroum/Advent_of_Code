import src  # My utility functions
import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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


def animate(x, y, vx, vy, t=np.arange(20_000), interval=None):
    interval = interval or int(1000 * (t[-1] - t[0]) / len(t))
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    ax.set_facecolor('0.0')
    scat = ax.scatter(x + t[0] * vx, y + t[0] * vy, c='#ffff50')

    def update(i):
        x_i = x + t[i] * vx
        y_i = y + t[i] * vy
        scat.set_offsets(np.array([x_i, y_i]).T)
        return scat,

    return src.Player(fig, update, interval=interval, frames=len(t))


def main():
    ans2 = find_message(X, Y, VX, VY)
    print("Part One:")
    print("Plotted the message in a new window.")  # ERCXLAJL

    print("\nPart Two:")
    print(f"The message would have appeared after {ans2} seconds.")  # 10813
    src.clip(ans2)

    print("\nBonus:")
    print(f"Animating the points of light around {ans2} seconds...")
    return ans2


if __name__ == '__main__':
    message_time = main()
    anim = animate(X, Y, VX, VY, t=np.linspace(message_time-5, message_time+5, 251))
