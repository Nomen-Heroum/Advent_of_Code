import src  # My utility functions

RULES = src.read()


def parse(rule):
    bag, contents = rule.split(' bags contain ')
    if 'no other' in contents:
        return bag, {}
    bagsin = contents.split(', ')
    content_dict = {' '.join(b.split()[1:3]): int(b.split()[0]) for b in bagsin}
    return bag, content_dict


def parse_all(rules=RULES):
    tuples = (parse(r) for r in rules)
    return {k: v for k, v in tuples}


RULES_DICT = parse_all()


def fits_in(rules=RULES, first_bag='shiny gold'):
    bags = [first_bag]
    new = 1
    while new > 0:
        new = 0
        for rule in rules:
            bag, contents = parse(rule)
            if bag not in bags and any(b in contents for b in bags):
                bags.append(bag)
                new += 1
    return len(bags) - 1


def has_in(rules=None, bag='shiny gold'):
    rules = rules if rules else RULES_DICT

    if rules[bag]:
        return sum((has_in(bag=key)+1) * val for (key, val) in rules[bag].items())
    return 0


def main():
    print("Part One:")
    fits = fits_in()
    print(f"There are {fits} bags your shiny gold bag can go in.")
    src.clip(fits)

    print("\nPart Two:")
    has = has_in()
    print(f"There are {has} bags in your golden bag.")
    src.clip(has)


if __name__ == '__main__':
    main()
