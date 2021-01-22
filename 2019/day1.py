import src  # My utility functions

MASSES = src.read(ints=True)


def fuel_requirement(mass):
    fuel = mass // 3 - 2
    if fuel > 0:
        return fuel + fuel_requirement(fuel)
    else:
        return 0


def main(masses=None):
    masses = masses or MASSES

    print("Part One:")
    ans1 = sum(m // 3 - 2 for m in masses)  # 3412531
    print(f"The total fuel requirement is {ans1}.")

    print("\nPart Two:")
    ans2 = sum(fuel_requirement(m) for m in masses)  # 5115927
    print(f"The total fuel requirement accounting for fuel mass is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
