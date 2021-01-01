import src

# Nodes contain all generator floors, then all respective microchip floors, then the current floor.
# Floors are numbered as their distance from the 4th floor, for nicer heuristic calculation.
START = ((3, 3, 3, 3, 3, 2, 3, 2, 3, 3), 3)
TARGET = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0)

START_2 = ((3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3), 3)
TARGET_2 = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0)


def neighbours(node):
    """Yields all neighbouring nodes and their cost (1)."""
    objects, current = node
    new_floors = []
    if current < 3:  # Can go downstairs
        new_floors.append(current + 1)
    if current > 0:  # Can go upstairs
        new_floors.append(current - 1)

    def move(obj):
        for i, flo in enumerate(obj):
            if flo == current:
                yield i, obj[:i] + (new,) + obj[i + 1:]

    half = len(objects)//2

    def is_valid(obj):
        generators = obj[:half]
        microchips = obj[half:]
        for m, mic in enumerate(microchips):
            if generators[m] != mic and mic in generators:  # Microchip is with a generator but not with its own
                return False
        return True

    for new in new_floors:  # For all possible directions
        for num, single_move in move(objects):
            if is_valid(single_move):
                yield (single_move, new), 1  # Move one object

            for _, second_move in move(objects[num + 1:]):
                two_moves = single_move[:num + 1] + second_move
                if is_valid(two_moves):
                    yield (two_moves, new), 1  # Move two objects


def heuristic(node, _target):
    """Returns the minimum move count assuming no restrictions. Admissible. Underestimates the move count
    when there is one object on the current floor and none below it."""
    return 2 * sum(node[0]) - 3 * node[1]


def main():
    src.one()
    ans1 = src.a_star(START, TARGET, heuristic, neighbours)
    print(f"You need at least {ans1} steps.")

    src.two()
    ans2 = src.a_star(START_2, TARGET_2, heuristic, neighbours)
    print(f"With the extra objects, the minimum is {ans2} steps.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
