import src
import heapq
from copy import deepcopy

STRINGS = src.read()


def dijkstra(start, search_space, targets):
    """Dijkstra pathfinding that prioritises path length, then reading order.
    Returns the neighbouring square the unit must move to, and which square it attacks (if any)."""
    def neighbours(xy):
        x, y = xy
        yield x - 1, y  # In reading order
        yield x, y - 1
        yield x, y + 1
        yield x + 1, y

    queue = [(0, start)]  # Path length, node
    visited = {start: None}  # Stores the previous node for each visited node
    move = None
    attack = None
    while queue:
        length, node = heapq.heappop(queue)
        if node in targets:
            previous = visited[node]
            if length > 1:  # Not next to a target; move one square
                while previous != start:  # Reconstruct the path taken
                    node = previous
                    previous = visited[node]
                move = node
            if length <= 2:  # Within range of a target; attack
                next_to = set(neighbours(move or start)) & targets.keys()
                attack = min(next_to, key=lambda k: (targets[k], k))  # Sort by HP, then reading order
            return move, attack
        for neigh in neighbours(node):
            if neigh in search_space - visited.keys():
                visited[neigh] = node
                heapq.heappush(queue, (length + 1, neigh))

    return move, attack  # No path found to any target


def map_out(strings, hit_points=200):
    space = set()
    elves = {}
    goblins = {}
    for x, string in enumerate(strings):
        for y, char in enumerate(string):
            pos = x, y  # Up/down as first coordinate for easier reading order sorting
            if char != '#':
                space.add(pos)
                if char == 'E':
                    elves[pos] = hit_points
                elif char == 'G':
                    goblins[pos] = hit_points
    return elves, goblins, space


def battle(elves, goblins, space, elf_attack=3, goblin_attack=3, version=1):
    rounds_completed = 0
    while elves and goblins:
        turns = sorted(elves.keys() | goblins.keys())
        for unit in turns:
            if unit in elves.keys() | goblins.keys():  # Hasn't been killed in this round
                is_elf = unit in elves
                allies = elves if is_elf else goblins
                targets = goblins if is_elf else elves
                if not targets:
                    total_hp = sum(allies.values())
                    print(f"Combat ends after {rounds_completed} full rounds.\n"
                          f"{'Elves' if is_elf else 'Goblins'} win with {total_hp} total hit points left.")
                    return rounds_completed * total_hp
                move, attack = dijkstra(unit, space - allies.keys(), targets)
                if move:
                    hit_points = allies[unit]
                    del allies[unit]
                    allies[move] = hit_points
                if attack:
                    targets[attack] -= elf_attack if is_elf else goblin_attack  # Reduce target HP
                    if targets[attack] <= 0:
                        if version > 1 and not is_elf:
                            return None
                        del targets[attack]
        rounds_completed += 1


def main(strings=STRINGS):
    args = map_out(strings)

    print("Part One:")
    ans1 = battle(*deepcopy(args))  # 195811
    print(f"The outcome of this battle is {ans1}.")

    print("\nPart Two:")
    elf_attack = 3
    ans2 = None
    while not ans2:
        elf_attack += 1
        ans2 = battle(*deepcopy(args), elf_attack=elf_attack, version=2)
    print(f"The elves need an attack power of {elf_attack}; the outcome is {ans2}.")  # 69867
    src.clip(ans2)


if __name__ == '__main__':
    main()
