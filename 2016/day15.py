import src
from parse import parse

STRINGS = src.read(15)


def sieve(strings, version=1):
    time = 0
    step = 1
    for s in strings:
        disc, positions, start = parse('Disc #{:d} has {:d} positions; at time=0, it is at position {:d}.', s)
        while (time + disc + start) % positions != 0:
            time += step
        step *= positions
    if version > 1:
        while (time + 7) % 11 != 0:
            time += step
    return time


def main(strings=STRINGS):
    print("Part One:")
    ans1 = sieve(strings)
    print(f"The first time at which you can press the button is {ans1}.")

    print("\nPart Two:")
    ans2 = sieve(strings, version=2)
    print(f"With the extra disc, the first time is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
