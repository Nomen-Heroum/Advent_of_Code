import src
import math

strings = src.read()


def count_trees(right, down, field=strings):
    row = 0
    column = 0
    modulus = len(field[0])
    trees = 0
    while row < len(field):
        if field[row][column % modulus] == '#':
            trees += 1
        row += down
        column += right
    print(f"# of trees encountered going right {right} & down {down}: {trees} out of {len(field)}.")
    return trees


print("Part One:")
count_trees(3, 1)

print("\nPart Two:")
slopes = [(1, 1),
          (3, 1),
          (5, 1),
          (7, 1),
          (1, 2)]

tree_counts = [count_trees(*t) for t in slopes]

print(f"The product of these tree counts is {math.prod(tree_counts)}.")
