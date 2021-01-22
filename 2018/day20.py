import src  # My utility functions
from copy import copy

REGEX = src.read()[0]
DIRECTIONS = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}


def map_out(regex, directions=None):
    directions = directions or DIRECTIONS

    positions = {0}
    split_starts = []
    split_ends = []
    visited = {0: 0}  # Distance for each room
    for char in regex[1:-1]:  # Excluding the ^$
        if char == '(':
            split_starts.append(copy(positions))  # Store the locations before the split
            split_ends.append(set())  # New set to store split results in
        elif char == '|':
            split_ends[-1] |= positions
            positions = copy(split_starts[-1])  # Go back to the beginning of the split
        elif char == ')':
            positions |= split_ends.pop()  # Add the rest of the final positions
            split_starts.pop()
        else:  # N, E, S, or W
            new_positions = set()
            while positions:  # For every current position:
                pos = positions.pop()
                distance = visited[pos]  # Get the distance
                pos += directions[char]  # Move
                if pos not in visited:
                    visited[pos] = distance + 1  # Store the new distance
                new_positions.add(pos)  # And the new position
            positions = new_positions
    return max(visited.values()), len([v for v in visited.values() if v >= 1000])


def main(regex=REGEX):
    ans1, ans2 = map_out(regex)
    print("Part One:")
    print(f"The furthest away room has me go through {ans1} doors.")  # 4308

    print("\nPart Two:")
    print(f"There are {ans2} rooms that have me go through at least 1000 doors.")  # 8528
    src.clip(ans2)


if __name__ == '__main__':
    main()
