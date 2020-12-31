import src
import heapq

# 5-tuple containing all four floors in order, then the current floor number
START = ((frozenset({'Po', 'Tm', 'Pm', 'Ru', 'Co'}), frozenset({'Tm', 'Ru', 'Co'})),  # frozensets are hashable
         (frozenset(), frozenset({'Po', 'Pm'})),
         (frozenset(), frozenset()),
         (frozenset(), frozenset()),
         1)  # Current floor

TARGET = ((frozenset(), frozenset()),
          (frozenset(), frozenset()),
          (frozenset(), frozenset()),
          (frozenset({'Po', 'Tm', 'Pm', 'Ru', 'Co'}), frozenset({'Po', 'Tm', 'Pm', 'Ru', 'Co'})),
          4)  # End on the 4th floor


def neighbours(node):
    pass  # TODO


def heuristic(node, _target):
    """Returns the minimum move count assuming no restrictions"""
    current_floor_dist = 4 - node[-1]  # Current distance to 4th floor
    h = 0
    for floor, (generators, microchips) in enumerate(node[:-2]):
        floor_dist = 3 - floor  # Distance to 4th floor
        object_count = len(generators) + len(microchips)

        # If there is only one object on this floor and none below it
        if floor_dist == current_floor_dist and not h and object_count < 2:
            h += current_floor_dist

        h += 2 * floor_dist * object_count
    h -= 3 * current_floor_dist
    return h


def a_star(start, target, h, neighbours_costs):
    """Generic A* pathfinding algorithm. Does not return a path, only the discovered path length.

    A binary heap (heapq) is used for the priority queue. f(n) = g(n) + h(n) is prioritised as always.
    In case of a tie, the node with the lowest heuristic h(n) is prioritised. Further ties are handled
    in reverse insertion order (Last In, First Out).

    Nodes are stored in sets, so they must be hashable.

    Args:
        start: The starting node.
        target: The target node.
        h: A function that returns the heuristic h(n) of a given node. Takes two arguments: (node, target)
        neighbours_costs: A single-argument function that takes the current node, and yields tuples containing
            each neighbouring node and its distance from the current node: (neighbour, cost)

    Returns:
        The length of the discovered path.
    """
    guess = h(start, target)  # Best guess for the shortest path length
    entry_id = 0

    # Priority queue: f(n) is prioritised, with ties broken first by h(n), then by last inserted.
    queue = [(guess, guess, entry_id, start, 0)]  # (f(n), h(n), entry, node, g(n))

    to_visit = {start}  # Set containing the same nodes as the queue; prevents duplicates
    visited = set()

    while to_visit:
        _f, _h, _id, node, g = heapq.heappop(queue)
        to_visit.remove(node)
        visited.add(node)
        for neigh, cost in neighbours_costs(node):
            if neigh == target:  # Bingo!
                return g + cost
            if neigh not in visited | to_visit:
                entry_id -= 1  # Negative to ensure LIFO
                g += cost  # Update path length
                h_n = h(neigh, target)
                heapq.heappush(queue, (g + h_n, h_n, entry_id, neigh, g))
                to_visit.add(neigh)

    # If every possible node has been visited
    raise EOFError("No path to the target could be found.")


def main(parent=START, target=TARGET):
    src.one()
    ans1 = a_star(parent, target, heuristic, neighbours)
    print(f"You need at least {ans1}.")

    src.copy(ans1)


if __name__ == '__main__':
    main()
