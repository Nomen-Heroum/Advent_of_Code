import src
import heapq

# Nodes contain all generator floors, then all respective microchip floors, then the current floor.
# Floors are numbered as their distance from the 4th floor, for nicer heuristic calculation.
START = ((3, 3, 3, 3, 3, 2, 3, 2, 3, 3), 3)
TARGET = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0)


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

    def is_valid(obj):
        generators = obj[:5]
        microchips = obj[-5:]
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


def a_star(start, target, h, neighbours_costs, admissible=True):
    """Generic A* pathfinding algorithm. Does not return a path, only the discovered path length.

    A binary heap (heapq) is used for the priority queue. f(n) = g(n) + h(n) is prioritised as always.
    In case of a tie, the node with the lowest heuristic h(n) is prioritised. Further ties are handled
    in reverse insertion order (Last In, First Out).

    Different algorithms are used for admissible and non-admissible heuristics; the admissible case is
    faster, but it breaks for improper heuristics.

    Nodes are stored in sets, so they must be hashable.

    Args:
        start: The starting node.
        target: The target node.
        h: A function that returns the heuristic h(n) of a given node. Takes two arguments: (node, target)
        neighbours_costs: A single-argument function that takes the current node, and yields tuples containing
            each neighbouring node and its distance from the current node: (neighbour, cost)
        admissible (optional): True if the heuristic is admissible (default), False otherwise. Must be set to
            False for non-admissible heuristics to prevent breakage.

    Returns:
        The length of the discovered path.
    """
    guess = h(start, target)  # Best guess for the shortest path length
    entry_id = 0

    # Priority queue: f(n) is prioritised, with ties broken first by h(n), then by last inserted.
    queue = [(guess, guess, entry_id, start, 0)]  # (f(n), h(n), entry, node, g(n))

    if admissible:  # Faster, more breakable algorithm
        visited = {start}

        while queue:
            _f, _h, _id, node, g = heapq.heappop(queue)
            for neigh, cost in neighbours_costs(node):
                if neigh == target:  # Return straight away when we touch the target node
                    return g + cost
                if neigh not in visited:
                    entry_id -= 1  # Negative to ensure LIFO
                    g_n = g + cost
                    h_n = h(neigh, target)
                    f_n = g_n + h_n  # Total path cost
                    heapq.heappush(queue, (f_n, h_n, entry_id, neigh, g_n))
                    visited.add(neigh)  # We mark the neighbours as visited to prevent duplicates

    else:  # Slower, more resilient algorithm
        visited = set()

        while queue:
            _f, _h, _id, node, g = heapq.heappop(queue)
            if node == target:  # Only return once the target node is current
                return g
            if node not in visited:
                visited.add(node)  # Without an admissible h(n) we have to mark the current node as visited
                for neigh, cost in neighbours_costs(node):
                    if neigh not in visited:
                        entry_id -= 1  # Negative to ensure LIFO
                        g_n = g + cost
                        h_n = h(neigh, target)
                        f_n = g_n + h_n  # Total path cost
                        heapq.heappush(queue, (f_n, h_n, entry_id, neigh, g_n))

    # If every possible node has been visited
    raise EOFError("No path to the target could be found.")


def main(parent=START, target=TARGET):
    src.one()
    ans1 = a_star(parent, target, heuristic, neighbours)
    print(f"You need at least {ans1} steps.")

    src.copy(ans1)


if __name__ == '__main__':
    main()
