import src  # My utility functions
from copy import copy

STRINGS = src.read()
mid_x = len(STRINGS) // 2
mid_y = len(STRINGS[0]) // 2
START = {(y - mid_y) + (mid_x - x) * 1j  # Place the infected nodes in the complex plane, middle is 0 and up is i
         for x, s in enumerate(STRINGS)
         for y, c in enumerate(s)
         if c == '#'}


def count_infections(start: set, bursts=10_000):
    infected = copy(start)
    direction = 1j
    current = 0
    infection_count = 0
    for _ in range(bursts):
        if current in infected:
            direction *= -1j
            infected.remove(current)
        else:
            direction *= 1j
            infected.add(current)
            infection_count += 1
        current += direction
    return infection_count


def count_infections_evolved(start: set, bursts=10_000_000):
    print("Infecting...\r", end='')
    status = {k: '#' for k in start}
    direction = 1j
    current = 0
    infection_count = 0
    for _ in range(bursts):
        if current not in status:
            direction *= 1j
            status[current] = 'W'
        elif status[current] == 'W':
            status[current] = '#'
            infection_count += 1
        elif status[current] == '#':
            direction *= -1j
            status[current] = 'F'
        else:  # Status is 'F'
            direction *= -1
            del status[current]
        current += direction
    return infection_count


def main(start=None):
    start = start or START

    print("Part One:")
    ans1 = count_infections(start)  # 5538
    print(f"Out of 10,000 bursts of activity, {ans1} cause an infection.")

    print("\nPart Two:")
    ans2 = count_infections_evolved(start)  # 2511090
    print(f"Out of 10,000,000 evolved bursts, {ans2} cause an infection.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
