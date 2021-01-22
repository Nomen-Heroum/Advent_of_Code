import src  # My utility functions
from cmath import phase

STRINGS = src.read()


def build_station(strings):
    asteroids = {y + x * 1j for y, string in enumerate(strings)
                 for x, char in enumerate(string) if char == '#'}

    seen_from_base = {}
    for asteroid in asteroids:
        seen = {}
        for other in asteroids - {asteroid}:
            rotation = phase(other - asteroid)
            if rotation not in seen:
                seen[rotation] = other
        if len(seen) > len(seen_from_base):
            seen_from_base = seen
    winning_asteroid = seen_from_base[sorted(seen_from_base, reverse=True)[199]]
    return len(seen_from_base), int(100 * winning_asteroid.imag + winning_asteroid.real)


def main(strings=STRINGS):
    ans1, ans2 = build_station(strings)
    print("Part One:")
    print(f"The best location oversees {ans1} other asteroids.")  # 274

    print("\nPart Two:")
    print(f"The winning asteroid gives a value of {ans2}.")  # 305
    src.clip(ans2)


if __name__ == '__main__':
    main()
