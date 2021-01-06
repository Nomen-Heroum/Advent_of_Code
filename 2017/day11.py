import src

PATH = src.read()[0]
DIRECTIONS = {'nw': -1, 'n': 1j, 'ne': 1+1j,
              'sw': -1-1j, 's': -1j, 'se': 1}


def shortest_path(path, directions=None):
    directions = directions or DIRECTIONS

    location = 0
    furthest = 0
    distance = 0
    for p in path.split(','):
        location += directions[p]
        x, y = int(location.real), int(location.imag)
        if (x < 0) == (y < 0):
            distance = max(abs(x), abs(y))
        else:
            distance = abs(x) + abs(y)
        furthest = max(furthest, distance)

    return distance, furthest


def main(path=PATH):
    ans1, ans2 = shortest_path(path)
    print("Part One:")
    print(f"It takes at least {ans1} steps to reach the child process.")  # 764

    print("\nPart Two:")
    print(f"The furthest the child process got was {ans2} steps away.")  # 1532
    src.copy(ans2)


if __name__ == '__main__':
    main()
