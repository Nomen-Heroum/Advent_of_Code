import src  # My utility functions
import numpy as np
from scipy.stats import mode

STRINGS = src.read()


def power_consumption(arr):
    modes = mode(arr)[0][0]  # Find the most common digit in all columns
    n = modes.size
    sigma = modes[::-1].dot(2**np.arange(n))  # Convert to binary
    epsilon = 2**n - 1 - sigma
    return sigma * epsilon


def life_support_rating(arr):
    def bit_criteria(column):
        [most_common], [count] = mode(column)
        return 1 if count == column.size/2 else most_common

    columns = arr.shape[1]
    oxygen = co2 = arr
    for i in range(columns):
        ox_column = oxygen[:, i]
        oxygen = oxygen[ox_column == bit_criteria(ox_column)]
        if len(oxygen) == 1:
            break
    for i in range(columns):
        co_column = co2[:, i]
        co2 = co2[co_column != bit_criteria(co_column)]
        if len(co2) == 1:
            break

    binary_powers = 2**np.arange(columns)[::-1]
    return oxygen[0].dot(binary_powers) * co2[0].dot(binary_powers)


def main(strings=STRINGS):
    arr = np.genfromtxt(strings, int, delimiter=1)  # Cast all 0s and 1s into a 2D array
    print("Part One:")
    ans1 = power_consumption(arr)  # 3895776
    print(f"The power consumption of the sub is {ans1}.")

    print("\nPart Two:")
    ans2 = life_support_rating(arr)  # 7928162
    print(f"The life support rating is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
