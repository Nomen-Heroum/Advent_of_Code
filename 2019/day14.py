import src  # My utility functions
import re
from collections import defaultdict

STRINGS = src.read()


def produce_fuel(strings, ore=1000_000_000_000):
    requirements = {}
    for s in strings:
        chemicals = re.split(', | => ', s)
        amounts = [c.split() for c in chemicals]
        output = amounts[-1]
        requirements[output[1]] = int(output[0]), {c[1]: int(c[0]) for c in amounts[:-1]}

    def calculate_ore(chem, amt):
        excess = defaultdict(int)

        def ore_required(chemical, amount):
            if excess[chemical]:
                if excess[chemical] >= amount:
                    excess[chemical] -= amount
                    return 0
                else:
                    amount -= excess[chemical]
                    excess[chemical] = 0
            produced, ingredients = requirements[chemical]
            repetitions = (amount - 1) // produced + 1
            excess[chemical] = (repetitions * produced) - amount
            return sum(repetitions * req if ingr == 'ORE' else ore_required(ingr, repetitions * req)
                       for ingr, req in ingredients.items())

        return ore_required(chem, amt)

    single_cost = calculate_ore('FUEL', 1)
    fuel_made = ore // single_cost
    while True:
        cost = calculate_ore('FUEL', fuel_made)
        extra_cost = calculate_ore('FUEL', fuel_made + 1)
        if cost <= ore < extra_cost:
            break
        extra = (ore - cost) // (extra_cost - cost)
        fuel_made += extra

    return single_cost, fuel_made


def main(strings=STRINGS):
    ans1, ans2 = produce_fuel(strings)
    print("Part One:")
    print(f"{ans1} ORE is needed to produce 1 FUEL.")  # 337862

    print("\nPart Two:")
    print(f"I can make {ans2} fuel out of a trillion units of ore.")  # 3687786
    src.clip(ans2)


if __name__ == '__main__':
    main()
