import src
import re
import itertools

# Store a tuple with (depth, range, period) for each scanner
FIREWALL = [(int(d), int(r), 2 * (int(r) - 1)) for d, r in re.findall(r'(\d+): (\d+)', src.read('\n\n')[0])]


def severity(firewall):
    return sum(d * r for d, r, p in firewall[1:] if d % p == 0)


def minimum_delay(firewall):             # Quick and dirty optimisation:
    for delay in itertools.count(2, 2):  # Delay must be even because of the scanner with range 2 at depth 1
        if all((d + delay) % p for d, _, p in firewall):
            return delay


def main(firewall=None):
    firewall = firewall or FIREWALL

    print("Part One:")
    ans1 = severity(firewall)  # 648
    print(f"The severity of my trip is {ans1}.")

    print("\nPart Two:")
    ans2 = minimum_delay(firewall)  # 3933124
    print(f"The minimum delay to stay undetected is {ans2} picoseconds.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
