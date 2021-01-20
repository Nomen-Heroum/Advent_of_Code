import src
from collections import Counter

NUMBERS = src.read(' ', ints=True)' ')]


def build_dict(numbers: list, _return_length=False):
    child_amount, meta_amount = numbers[:2]
    index = 2
    children = []
    for _ in range(child_amount):
        node_dict, node_length = build_dict(numbers[index:], True)
        children.append(node_dict)
        index += node_length
    length = index + meta_amount
    metadata = numbers[index:length]
    node_dict = {'children': children, 'metadata': metadata}
    if _return_length:
        return node_dict, length
    return node_dict


def checksum(node_dict: dict):
    total = sum(node_dict['metadata'])
    for child in node_dict['children']:
        total += checksum(child)
    return total


def value(node_dict: dict):
    if not node_dict['children']:
        return sum(node_dict['metadata'])
    else:
        total = 0
        child_amount = len(node_dict['children'])
        meta_dict = Counter(n for n in node_dict['metadata'] if n <= child_amount)
        for child_id, number in meta_dict.items():
            total += number * value(node_dict['children'][child_id - 1])
        return total


def main(numbers=None):
    numbers = numbers or NUMBERS

    node_dict = build_dict(numbers)

    print("Part One:")
    ans1 = checksum(node_dict)  # 46096
    print(f"The total metadata checksum is {ans1}.")

    print("\nPart Two:")
    ans2 = value(node_dict)  # 24820
    print(f"The value of the root node is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
