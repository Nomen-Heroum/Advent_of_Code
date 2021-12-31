import src  # My utility functions
import heapq
import string

STRINGS = src.read()


def map_out(strings: list):
    maze = set()
    start = 0
    keys = {}
    doors = {}
    for x, s in enumerate(strings):
        for y, char in enumerate(s):
            if char != '#':
                coord = x + y * 1j
                if char in string.ascii_uppercase:
                    doors[coord] = char
                else:
                    maze.add(coord)
                    if char == '@':
                        start = coord
                    elif char != '.':
                        keys[coord] = char
    return (start, frozenset()), frozenset(maze), keys, doors


START, MAZE, KEYS, DOORS = map_out(STRINGS)


def neighbours(node, maze, keys, doors):
    coord, keys_found = node
    for move in (-1, -1j, 1, 1j):
        new_coord = coord + move
        if new_coord in maze:
            if new_coord in keys:
                yield new_coord, keys_found | {keys[new_coord]}
            else:
                yield new_coord, keys_found
        elif new_coord in doors and doors[new_coord].lower() in keys_found:
            yield new_coord, keys_found


def neighbours_multiple(node, maze, keys, doors):
    bots, keys_found = node
    for bot in bots:
        for b, k in neighbours((bot, keys_found), maze, keys, doors):
            yield bots - {bot} | {b}, k


def dijkstra(neighs, start, maze, keys, doors):
    """Dijkstra pathfinding algorithm, adapted from src.a_star"""
    keys = keys or KEYS
    doors = doors or DOORS

    print("Working...\r", end='')
    entry_id = 0

    # Priority queue: g(n) is prioritised, with ties broken by last inserted.
    queue = [(0, entry_id, start)]  # (g(n), entry, node)

    visited = {start}
    n = len(keys)

    g_max = 0
    while queue:
        g, _id, node = heapq.heappop(queue)
        if g > g_max:
            g_max = g
            print(f"{g} steps investigated...\r", end='')
        for neigh in neighs(node, maze, keys, doors):
            if len(neigh[1]) == n:  # Return when there are no more important locations
                return g + 1
            if neigh not in visited:
                entry_id -= 1  # Negative to ensure LIFO
                g_n = g + 1
                heapq.heappush(queue, (g_n, entry_id, neigh))
                visited.add(neigh)  # We mark the neighbours as visited to prevent duplicates

    # If every possible node has been visited
    raise EOFError("No path to the target could be found.")


def main(strings=STRINGS):
    start, maze, keys, doors = map_out(strings)

    print("Part One:")
    ans1 = dijkstra(neighbours, start, maze, keys, doors)  # 4204
    print(f"I need to take at least {ans1} steps to collect all keys.")

    print("\nPart Two:")  # TODO: Try removing dead ends
    mid = start[0]
    vaults = maze - {mid, mid - 1, mid - 1j, mid + 1, mid + 1j}
    bots = frozenset({mid-1-1j, mid-1+1j, mid+1-1j, mid+1+1j})
    ans2 = dijkstra(neighbours_multiple, (bots, frozenset()), vaults, keys, doors)  # TODO: Comment result.
    print(f"With four bots, I can collect the keys in {ans2} steps.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
