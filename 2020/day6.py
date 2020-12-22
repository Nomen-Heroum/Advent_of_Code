import src

GROUPS = src.read(6, split='\n\n')


def any_count(group: str):
    return len(set(group.replace('\n', '')))


def all_count(group: str):
    answers = set(group.replace('\n', ''))
    members = group.split('\n')
    return sum(all(char in m for m in members) for char in answers)


def main(groups=GROUPS):
    print("Part One:")
    total = sum(any_count(g) for g in groups)
    print(f"Total questions answered yes is {total}.")
    src.copy(total)

    print("\nPart Two:")
    total2 = sum(all_count(g) for g in groups)
    print(f"Total questions answered yes is {total2}.")
    src.copy(total2)


if __name__ == '__main__':
    main()
