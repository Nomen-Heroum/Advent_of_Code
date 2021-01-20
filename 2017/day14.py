import src
import functools
import operator

KEY = 'stpzcrnm'


def knot(string: str, size=256):
    """Adapted Knot Hash from day 10, outputs 128 bit binary string."""
    lengths = [ord(c) for c in string] + [17, 31, 73, 47, 23]

    lst = list(range(size))
    first_pos = 0  # Keep track of the position of the first element when we rotate the list
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            lst[:length] = lst[:length][::-1]
            rotation = (length + skip_size) % size
            lst = lst[rotation:] + lst[:rotation]  # Rotate the list
            first_pos -= rotation
            skip_size += 1
    first_pos %= size
    lst = lst[first_pos:] + lst[:first_pos]  # Put the first element back in front

    blocks = (lst[i:i + 16] for i in range(0, size, 16))
    dense_hash = [functools.reduce(operator.xor, b) for b in blocks]
    knot_hash = ''
    for n in dense_hash:
        knot_hash += format(n, '08b')
    return knot_hash


def build_grid(key: str):
    grid = set()
    for i in range(128):
        for j, char in enumerate(knot(f"{key}-{i}")):
            if char == '1':
                grid.add(i + j*1j)
    return len(grid), grid


def find_regions(grid: set):
    def build_region(node):
        for move in (-1, 1, -1j, 1j):
            new_node = node + move
            if new_node in grid:
                grid.remove(new_node)
                build_region(new_node)

    group_count = 0
    while grid:
        build_region(grid.pop())
        group_count += 1
    return group_count


def main(key=KEY):
    print("Part One:")
    ans1, grid = build_grid(key)  # 8250
    print(f"{ans1} squares are used in the grid.")

    print("\nPart Two:")
    ans2 = find_regions(grid)  # 1113
    print(f"There are {ans2} regions in the grid.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
