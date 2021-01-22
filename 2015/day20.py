import src  # My utility functions
import itertools

PRESENTS = 36000000


def first_house(presents):
    for address in itertools.count(831600):
        factors = set(itertools.chain.from_iterable(
            (i, address//i) for i in range(1, int(address**0.5) + 1) if address % i == 0))
        if sum(factors) * 10 >= presents:
            return address


def first_house2(presents):
    for address in itertools.count(831600):
        factors = set(address//i for i in range(1, 51) if address % i == 0)
        if sum(sorted(factors)[-50:]) * 11 >= presents:
            return address


def main(presents=PRESENTS):
    print("Part One:")
    first = first_house(presents)
    print(f"The first house to get {presents} presents is {first}.")

    print("\nPart Two:")
    first2 = first_house2(presents)
    print(f"The first house to get {presents} presents is {first2}.")
    src.clip(first2)


if __name__ == '__main__':
    main()
