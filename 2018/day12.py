import src  # My utility functions
import numpy as np
import matplotlib.pyplot as plt

INITIAL, RULES = src.read('\n\n')
PLANTS = {i for i, char in enumerate(INITIAL.split()[-1]) if char == '#'}
PATTERNS = {frozenset(i - 2 for i, char in enumerate(s[:5]) if char == '#')
            for s in RULES.splitlines() if s[-1] == '#'}


def iterate(plants: set, patterns: set, generations=20):
    history = [plants]  # For plotting
    for i in range(generations):
        new_plants = set()
        for pot in range(min(plants) - 2, max(plants) + 2):
            if {n - pot for n in set(range(pot - 2, pot + 3)) & plants} in patterns:
                new_plants.add(pot)
        history.append(new_plants)
        offset = sum(new_plants) - sum(plants)
        if offset % len(plants) == 0 and len(plants) == len(new_plants):
            # Setting up a plot
            min_all = min(min(p) for p in history)
            max_all = max(max(p) for p in history)
            width = max_all - min_all + 1
            hist_array = np.array([[int(y + min_all in p) for y in range(width)]
                                   for x, p in enumerate(history)])
            plt.imshow(hist_array, cmap='gray_r', extent=[min_all, max_all, len(history), 0])

            return sum(plants) + offset * (generations - i)
        plants = new_plants
    return sum(plants)


def main():
    print("Part One:")
    ans1 = iterate(PLANTS, PATTERNS)  # 2917
    print(f"The sum of inhabited pot numbers after 20 generations is {ans1}.")

    print("\nPart Two:")
    ans2 = iterate(PLANTS, PATTERNS, 50_000_000_000)  # 3250000000956
    print(f"after 50,000,000,000 generations, the sum is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
