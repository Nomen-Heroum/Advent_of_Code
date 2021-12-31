import src  # My utility functions
import numpy as np
from scipy.optimize import minimize

POSITIONS = np.array(src.read(split=',', ints=True))


def align(positions):
    median = int(np.median(positions))
    fuel_costs = abs(positions - median)
    return sum(fuel_costs)


def align_2_electric_boogaloo(positions):
    mean = int(positions.mean())
    distances = abs(positions - mean)
    return ((distances * (distances + 1)) // 2).sum()


def main(positions=POSITIONS):
    print("Part One:")
    ans1 = align(positions)  # 349357
    print(f"The crabs must spend {ans1} fuel to align.")

    print("\nPart Two:")
    ans2 = align_2_electric_boogaloo(positions)  # 96708205
    print(f"Actually, they have to spend {ans2} fuel.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
