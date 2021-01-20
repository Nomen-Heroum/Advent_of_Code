import src
import re
import itertools
import heapq

STRING = src.read(split='\n\n')[0]
NODES = re.findall(r'x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+%', STRING)  # Extract the numbers
NODES = [tuple(int(s) for s in tup) for tup in NODES]  # Convert to ints


def count_viable_pairs(nodes: list):
    viable = 0
    for (_x1, _y1, used1, avail1), (_x2, _y2, used2, avail2) in itertools.combinations(nodes, 2):
        if used1 and used1 <= avail2:
            viable += 1
        if used2 and used2 <= avail1:
            viable += 1
    return viable


def map_out(nodes):
    space = set()
    empty = ()
    x = 0
    for x, y, used, _ in nodes:
        if used < 100:
            space.add(x + y*1j)
            if not used:
                empty = x + y*1j
    assert empty, "No empty nodes found."
    return space, empty, x


SPACE, EMPTY, GOAL = map_out(NODES)


def neighbours(state, space=None):
    space = space or SPACE

    empty, goal = state
    for move in (-1, 1, -1j, 1j):
        new_empty = empty + move
        if new_empty in space:
            if new_empty == goal:
                yield goal, empty
            else:
                yield new_empty, goal


def heuristic(state):
    """Mostly admissible."""
    empty, goal = state
    near_edge = min(goal.real, goal.imag)
    far_edge = max(goal.real, goal.imag)
    dist = abs((empty - goal).real) + abs((empty - goal).imag)
    return dist - 1 + near_edge + 5 * far_edge


def a_star(start, h, neighs, space=None):
    """A* pathfinding algorithm from src.py, adapted for today's puzzle."""
    space = space or SPACE

    guess = h(start)  # Best guess for the shortest path length
    entry_id = 0

    # Priority queue: f(n) is prioritised, with ties broken first by h(n), then by last inserted.
    queue = [(guess, guess, entry_id, start, 0)]  # (f(n), h(n), entry, node, g(n))

    visited = {start}

    while queue:
        _f, _h, _id, node, g = heapq.heappop(queue)
        for neigh in neighs(node, space):
            if neigh[1] == 0:  # Return straight away when we touch the target node
                return g + 1
            if neigh not in visited:
                entry_id -= 1  # Negative to ensure LIFO
                g_n = g + 1
                h_n = h(neigh)
                f_n = g_n + h_n  # Total path cost
                heapq.heappush(queue, (f_n, h_n, entry_id, neigh, g_n))
                visited.add(neigh)  # We mark the neighbours as visited to prevent duplicates

    # If every possible node has been visited
    raise EOFError("No path to the target could be found.")


def main(nodes=None):
    nodes = nodes or NODES

    print("Part One:")
    ans1 = count_viable_pairs(nodes)  # 1034
    print(f"There are {ans1} viable pairs.")

    print("\nPart Two:")
    ans2 = a_star((EMPTY, GOAL), heuristic, neighbours)  # 261
    print(f"The fewest number of steps required is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
