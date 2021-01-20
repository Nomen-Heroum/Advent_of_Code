import src
import re

STRINGS = src.read()


def groups(strings):
    group = set()

    def build_group(prog):
        group.add(prog)
        for child in re.search('> (.*)', strings[prog])[1].split(', '):
            n = int(child)
            if n not in group:
                build_group(n)

    build_group(0)
    group_length = len(group)
    group_count = 1
    remaining = set(range(len(strings))) - group
    while remaining:
        group = set()
        build_group(remaining.pop())
        group_count += 1
        remaining -= group
    return group_length, group_count


def main(strings=STRINGS):
    ans1, ans2 = groups(strings)
    print("Part One:")
    print(f"The group connected to program 0 has size {ans1}.")  # 169

    print("\nPart Two:")
    print(f"There are {ans2} groups.")  # 179
    src.clip(ans2)


if __name__ == '__main__':
    main()
