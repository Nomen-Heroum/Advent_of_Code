import src  # My utility functions
from collections import Counter
import parse

STRINGS = src.read()
PATTERN = parse.compile('{:d},{:d} -> {:d},{:d}')


def scan_obstacles(strings, version=1):
    obstacles = Counter()
    for string in strings:
        x1, y1, x2, y2 = PATTERN.parse(string)
        if version == 2 or x1 == x2 or y1 == y2:
            z1 = x1 + y1*1j
            z2 = x2 + y2*1j
            distance = max(abs(x2 - x1), abs(y2 - y1))
            step = (z2 - z1) / distance
            for i in range(distance + 1):
                obstacles[z1 + i * step] += 1
    return len([pos for pos, count in obstacles.items() if count > 1])


def main(strings=STRINGS):
    print("Part One:")
    ans1 = scan_obstacles(strings)  # 8622
    print(f"At least 2 straight lines overlap in {ans1} points.")

    print("\nPart Two:")
    ans2 = scan_obstacles(strings, version=2)  # 22037
    print(f"Including diagonals, at least 2 lines overlap in {ans2} points.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
