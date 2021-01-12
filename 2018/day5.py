import src
import string
import re

POLYMER = src.read()[0]


def react(polymer):
    encountered = []
    length = len(polymer)
    for char in polymer[1:]:
        if encountered and (char == char.upper() and encountered[-1] == char.lower()
                            or char == char.lower() and encountered[-1] == char.upper()):
            encountered.pop()
            length -= 2
        else:
            encountered.append(char)
    return length


def find_problem(polymer):
    shortest = len(polymer)
    for char in string.ascii_lowercase:
        new_polymer = re.sub(f'[{char}{char.upper()}]', '', polymer)
        shortest = min(shortest, react(new_polymer))
    return shortest


def main(polymer=POLYMER):
    ans1 = react(polymer)
    print("Part One:")
    print(f"After fully reacting the polymer, {ans1} units are left.")  # 11540

    print("\nPart Two:")
    ans2 = find_problem(polymer)
    print(f"The shortest possible polymer has length {ans2}.")  # 6918
    src.copy(ans2)


if __name__ == '__main__':
    main()
