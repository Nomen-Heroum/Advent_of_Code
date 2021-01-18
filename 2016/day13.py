import src
import copy

NUMBER = 1364
START = (1, 1)
TARGET = (31, 39)


def neighbours(node, number=NUMBER):
    def is_open(x, y):
        if x < 0 or y < 0:
            return False
        num = (x + y)**2 + 3*x + y + number
        if bin(num).count('1') % 2 == 0:
            return True
        return False

    x0, y0 = node
    neighs = ((x0 - 1, y0),
              (x0, y0 - 1),
              (x0 + 1, y0),
              (x0, y0 + 1))
    for new in neighs:
        if is_open(*new):
            yield new


def heuristic(node, target):
    return abs(target[0] - node[0]) + abs(target[1] - node[1])


def count_reach(start, steps):
    visited = {start}
    to_visit = {start}

    for _step in range(steps):
        new = set()
        for node in to_visit:
            for neigh in neighbours(node):
                if neigh not in visited:
                    visited.add(neigh)
                    new.add(neigh)
        to_visit = copy.deepcopy(new)

    return len(visited)


def main():
    print("Part One:")
    ans1 = src.a_star(START, TARGET, heuristic, neighbours)
    print(f"The minumum number of steps required is {ans1}.")

    print("\nPart Two:")
    ans2 = count_reach(START, 50)
    print(f"I can reach {ans2} locations in 50 steps.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
