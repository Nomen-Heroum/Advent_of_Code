import src  # My utility functions
import numpy as np

DEPTHS = np.array(src.read(ints=True))


def main(depths=DEPTHS):
    print("Part One:")
    ans1 = np.sum((depths[1:] - depths[:-1]) > 0)  # 1266
    print(f"{ans1} measurements are larger than the previous.")

    print("\nPart Two:")
    sum_depths = depths[:-2] + depths[1:-1] + depths[2:]
    ans2 = np.sum((sum_depths[1:] - sum_depths[:-1]) > 0)  # 1217
    print(f"There are {ans2} sliding window sum increases.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
