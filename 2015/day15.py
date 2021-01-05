import src
import parse
import numpy as np

STRINGS = src.read()
PATTERN = parse.compile("{}: capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}")


def ingredient_matrix(strings=STRINGS):
    return np.array([list(PATTERN.parse(s))[1:] for s in strings])


MATRIX = ingredient_matrix(STRINGS).T


def score(proportions, matrix=MATRIX):
    vector = np.array(proportions)
    product = matrix @ vector
    clipped = product.clip(min=0)
    return np.prod(clipped[:-1]), clipped[-1]


def high_score(calories=None):
    scores = []
    for x in range(101):
        for y in range(101 - x):
            for z in range(101 - x - y):
                points, cals = score([x, y, z, 100 - x - y - z])
                if (not calories) or (cals == calories):
                    scores.append(points)
    return max(scores)


def main(strings=STRINGS):
    print("Part One:")
    highest = high_score()
    print(f"The highest score is {highest}.")

    print("\nPart Two:")
    best = high_score(500)
    print(f"The highest score with 500 calories is {best}.")
    src.copy(best)


if __name__ == '__main__':
    main()
