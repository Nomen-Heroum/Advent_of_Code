import src  # My utility functions
import numpy as np

DEPTH = 9465
TARGET = 13, 704
WRONG_TOOLS = {0: 'neither',
               1: 'torch',
               2: 'gear'}


def erosion_level(geo_index, depth):
    return (geo_index + depth) % 20183


def risk_levels(depth, target):
    """Also returns the erosion levels, for later expansion."""
    goal_x, goal_y = target
    area = np.zeros((goal_y + 1, goal_x + 1), int)
    for x in range(1, goal_x + 1):
        area[0, x] = x * 16807  # First row (y = 0)
    area[0] = erosion_level(area[0], depth)
    for y in range(1, goal_y + 1):
        area[y, 0] = y * 48271  # First column (x = 0)
    area[1:, 0] = erosion_level(area[1:, 0], depth)

    for x in range(1, goal_x + 1):  # Filling out the rest of the grid
        for y in range(1, goal_y + 1):
            area[y, x] = erosion_level(area[y - 1, x] * area[y, x - 1], depth)
    area[goal_y, goal_x] = erosion_level(0, depth)

    risk = area % 3  # Finally reduce to risk levels
    return area, risk


def neighbours_costs(node, area, risk, depth):
    x, y, tools = node
    current_risk = risk[y, x]  # Current region type

    # Gear changes
    if current_risk == 0:  # Rocky region
        yield (x, y, 'torch' if tools == 'gear' else 'gear'), 7
    elif current_risk == 1:  # Wet region
        yield (x, y, 'neither' if tools == 'gear' else 'gear'), 7
    elif current_risk == 2:  # Narrow region
        yield (x, y, 'neither' if tools == 'torch' else 'torch'), 7

    # Moves
    for new_x, new_y in ((x-1, y), (x, y-1), (x+1, y), (x, y+1)):
        if new_x >= 0 and new_y >= 0:
            height, width = risk.shape
            if new_y == height:  # Add a new row
                area.resize((height+1, width), refcheck=False)
                risk.resize((height+1, width), refcheck=False)
                area[-1, 0] = erosion_level(height * 48271, depth)
                for x in range(1, width):
                    area[height, x] = erosion_level(area[height - 1, x] * area[height, x - 1], depth)
                risk[-1] = area[-1] % 3

            elif new_x == width:  # Add a new column
                for array in area, risk:
                    old = array.copy()
                    array.resize((height, width+1), refcheck=False)
                    array[:, :-1] = old
                area[0, -1] = erosion_level(width * 16807, depth)
                for y in range(1, height):
                    area[y, width] = erosion_level(area[y - 1, width] * area[y, width - 1], depth)
                risk[:, -1] = area[:, -1] % 3

            new_risk = risk[new_y, new_x]

            if tools != WRONG_TOOLS[new_risk]:
                yield (new_x, new_y, tools), 1


def heuristic(node, target):
    """Simple Manhattan distance."""
    return abs(target[0] - node[0]) + abs(target[1] - node[1])


def main(target=TARGET, depth=DEPTH):
    print("Part One:")
    area, risk = risk_levels(depth, target)
    ans1 = risk.sum()  # 9940
    print(f"The risk level of the relevant area is {ans1}.")

    print("\nPart Two:")
    ans2 = src.a_star((0, 0, 'torch'), (*target, 'torch'), heuristic, neighbours_costs, equal_weights=False,
                      risk=risk, area=area, depth=depth)  # 944
    print(f"The fastest I can reach the target is {ans2} minutes.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
