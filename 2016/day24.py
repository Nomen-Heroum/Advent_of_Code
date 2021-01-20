import src
import heapq

STRINGS = src.read()


def map_out(strings: list):
    maze = set()
    first = 0
    locations = set()
    for x, string in enumerate(strings):
        for y, char in enumerate(string):
            if char != '#':
                coord = x + y * 1j
                maze.add(coord)
                if char == '0':
                    first = coord
                elif char != '.':
                    locations.add(coord)
    start = first, frozenset(locations)  # Makes the node hashable
    return start, frozenset(maze)


START, MAZE = map_out(STRINGS)


def neighbours(node, maze=MAZE):
    coord, locations = node
    for move in (-1, -1j, 1, 1j):
        new_coord = coord + move
        if new_coord in maze:
            if new_coord in locations:
                yield new_coord, frozenset(set(locations) - {new_coord})
            else:
                yield new_coord, locations


def dijkstra(start, neighs, maze=MAZE):
    """Dijkstra pathfinding algorithm, adapted from src.a_star"""
    print("Working...\r", end='')
    entry_id = 0

    # Priority queue: g(n) is prioritised, with ties broken by last inserted.
    queue = [(0, entry_id, start)]  # (g(n), entry, node)

    visited = {start}
    ans1 = False  # Answer for part 1

    while queue:
        g, _id, node = heapq.heappop(queue)
        for neigh in neighs(node, maze):
            if not neigh[1]:  # Return when there are no more important locations
                if not ans1:
                    ans1 = g + 1
                if neigh[0] == start[0]:
                    return ans1, g + 1
            if neigh not in visited:
                entry_id -= 1  # Negative to ensure LIFO
                g_n = g + 1
                heapq.heappush(queue, (g_n, entry_id, neigh))
                visited.add(neigh)  # We mark the neighbours as visited to prevent duplicates

    # If every possible node has been visited
    raise EOFError("No path to the target could be found.")


def main():
    ans1, ans2 = dijkstra(START, neighbours)   # Effectively the Dijkstra algorithm
    print("Part One:")
    print(f"The fewest number of steps required is {ans1}.")  # 412

    print("\nPart Two:")
    print(f"If the robot has to come back, the fewest number of steps is {ans2}.")  # 664
    src.clip(ans2)


if __name__ == '__main__':
    main()
