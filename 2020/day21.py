import src
from parse import parse

STRINGS = src.read()


def extract_sets(strings):
    """Yields a set of ingredients and a set of allergens for each string"""
    for s in strings:
        ingredients, allergens = parse('{} (contains {})', s)
        ingr_set = set(ingredients.split())
        aller_set = set(allergens.split(', '))
        yield ingr_set, aller_set


def find_possibilities(strings):
    """Returns a dictionary of all possible ingredients for each allergen"""
    possible = {}
    for ingr_set, aller_set in extract_sets(strings):
        for allergen in aller_set:
            if allergen in possible:
                possible[allergen] &= ingr_set
            else:
                possible[allergen] = set(ingr_set)
    return possible


def count_impossible(strings):
    """Counts the total number of occurences of non-allergenic ingredients"""
    count = 0
    possible = set().union(*find_possibilities(strings).values())
    for ingr_set, _ in extract_sets(strings):
        count += len(ingr_set - possible)
    return count


def dangerous_ingredients(strings):
    """Returns the canonical dangerous ingredient string"""
    possible = find_possibilities(strings)
    found = {}
    while possible:
        new_possible = dict(possible)
        for aller, ingr_set in possible.items():
            if len(ingr_set) == 1:
                new_possible.pop(aller)
                for i in ingr_set:
                    found[aller] = i
                for ings in new_possible.values():
                    ings -= ingr_set
        possible = dict(new_possible)
    dangerous = dict(sorted(found.items())).values()
    return ','.join(dangerous)


def main(strings=STRINGS):
    print("Part One:")
    ans1 = count_impossible(strings)
    print(f"Ingredients that can't contain allergens appear {ans1} times.")

    print("\nPart Two:")
    ans2 = dangerous_ingredients(strings)
    print(f"The canonical dangerous ingredient list is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
