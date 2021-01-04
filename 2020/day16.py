import src
import re
from parse import parse
import math

INFO = src.read(16, split='\n\n')


def parse_info(info=INFO):
    rules = info[0].split('\n')
    rules_dict = {}
    for rule in rules:
        field, l1, h1, l2, h2 = parse('{}: {:d}-{:d} or {:d}-{:d}', rule)
        rules_dict[field] = lambda x, a=l1, b=h1, c=l2, d=h2: a <= x <= b or c <= x <= d
    my_ticket = [int(s) for s in re.findall(r'\d+', info[1])]
    other_tickets = [[int(s) for s in re.findall(r'\d+', line)] for line in info[2].split('\n')[1:]]
    return rules_dict, my_ticket, other_tickets


def error_rate(info):
    rules, _, other_tickets = parse_info(info)
    rate = 0
    valid = set()
    valid_tickets = []
    invalid = set()
    for ticket in other_tickets:
        good_ticket = True
        for value in ticket:
            if value in valid:
                continue
            elif value in invalid:
                rate += value
                good_ticket = False
            elif any(is_valid(value) for is_valid in rules.values()):
                valid.add(value)
            else:
                invalid.add(value)
                rate += value
                good_ticket = False
        if good_ticket:
            valid_tickets.append(ticket)
    return rate, valid_tickets


def departure_product(info, valid_tickets):
    rules, my_ticket = parse_info(info)[:2]
    n = len(rules)
    options = [list(rules.keys()) for _ in range(n)]
    found = []

    def clear(indx):
        opt = options[indx][0]
        found.append(opt)
        for index, opts in enumerate(options):
            if index != indx:
                try:
                    opts.remove(opt)
                except ValueError:
                    pass
                if len(opts) == 1 and options[index][0] not in found:
                    clear(index)

    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            if len(options[i]) > 1:
                for field in options[i]:
                    if not rules[field](value):
                        options[i].remove(field)
                        if len(options[i]) == 1:
                            clear(i)
    assert all(len(op) == 1 for op in options), "Some fields did not have one option."
    return math.prod(my_ticket[i] for i, opt in enumerate(options) if 'departure' in opt[0])


def main(info=INFO):
    print("Part One:")
    ans1, valid_tickets = error_rate(info)
    print(f"My scanning error rate is {ans1}.")

    print("\nPart Two:")
    ans2 = departure_product(info, valid_tickets)
    print(f"The product of my departure numbers is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
