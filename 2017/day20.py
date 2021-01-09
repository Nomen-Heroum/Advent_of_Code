import src
import parse
import pandas as pd
from copy import deepcopy

PATTERN = parse.compile('p=<{:d},{:d},{:d}>, v=<{:d},{:d},{:d}>, a=<{:d},{:d},{:d}>')
PARTICLES = pd.DataFrame([list(PATTERN.parse(s)) for s in src.read()])


def find_closest(particles, large=1e10):
    def d(p, v, a):
        return abs(a * large**2 / 2 + v * large + p)

    distances = []
    for i, (px, py, pz, vx, vy, vz, ax, ay, az) in enumerate(particles.values):
        distances.append((d(px, vx, ax) + d(py, vy, ay) + d(pz, vz, az), i))
    return min(distances)[1]


def collide(particles: pd.DataFrame):
    def is_sorted():
        for i in range(3):
            if not particles.sort_values(i).equals(particles.sort_values([i, i+3, i+6])):
                return False
        return True

    while not is_sorted():
        particles.values[:, 3:6] += particles.values[:, -3:]
        particles.values[:, :3] += particles.values[:, 3:6]
        particles.drop_duplicates(subset=[0, 1, 2], keep=False, inplace=True)
    return len(particles)


def main(particles=None):
    particles = particles or deepcopy(PARTICLES)

    print("Part One:")
    ans1 = find_closest(particles)  # 344
    print(f"The particle that stays closest on the long term is {ans1}.")

    print("\nPart Two:")
    ans2 = collide(particles)  # 404
    print(f"After all collisions, there are {ans2} particles left.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
