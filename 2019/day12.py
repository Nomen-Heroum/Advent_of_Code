import src  # My utility functions
import parse
import numpy as np
import itertools

STRINGS = src.read()
PATTERN = parse.compile('<x={:d}, y={:d}, z={:d}>')
MOONS = np.array([PATTERN.parse(s).fixed for s in STRINGS])


def simulate(moons, steps=1000):
    velocity = np.zeros_like(moons)
    for _ in range(steps):
        for i, moon in enumerate(moons[:-1]):
            for j, other in enumerate(moons[i+1:]):
                for coord in range(3):
                    if moon[coord] > other[coord]:
                        velocity[i, coord] -= 1
                        velocity[i+j+1, coord] += 1
                    elif moon[coord] < other[coord]:
                        velocity[i, coord] += 1
                        velocity[i+j+1, coord] -= 1
        moons += velocity
    return (abs(moons).sum(axis=1) * abs(velocity).sum(axis=1)).sum()


def find_repeat(moons):
    loop_lengths = []
    for coord in moons.T:
        start = coord.tobytes()
        velocity = np.zeros_like(coord)
        for iteration in itertools.count(1):
            for i in range(3):
                for j in range(i+1, 4):
                    if coord[i] > coord[j]:
                        velocity[i] -= 1
                        velocity[j] += 1
                    elif coord[i] < coord[j]:
                        velocity[i] += 1
                        velocity[j] -= 1
            coord += velocity
            new_bytes = coord.tobytes()
            if new_bytes == start and not velocity.any():
                loop_lengths.append(iteration)
                print(f"Coordinate looped with loop length {iteration}.")
                break
    return np.lcm.reduce(loop_lengths)


def main(moons=None):
    moons = moons or MOONS

    print("Part One:")
    ans1 = simulate(moons.copy())  # 12082
    print(f"The total energy after 1000 steps is {ans1}.")

    print("\nPart Two:")
    ans2 = find_repeat(moons.copy())  # 295693702908636
    print(f"A repeat is first achieved after {ans2} steps.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
