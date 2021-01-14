import src

RECIPES = 306281


def make_recipes(recipes):
    print("Producing recipes...\r", end='')

    produced = [3, 7]
    elf1 = 0
    elf2 = 1
    order = [int(n) for n in str(recipes)]
    found = False
    how_many = None
    while len(produced) < recipes + 10 or not found:
        recipe1 = produced[elf1]
        recipe2 = produced[elf2]
        tens, ones = divmod(recipe1 + recipe2, 10)
        if tens:
            produced.append(tens)
        produced.append(ones)

        if not found and order in (produced[-6:], produced[-7:-1]):
            found = True
            length = len(produced)
            how_many = length - 6 if order == produced[-6:] else length - 7

        mod = len(produced)
        elf1 += recipe1 + 1
        elf2 += recipe2 + 1
        elf1 %= mod
        elf2 %= mod

    return ''.join(str(n) for n in produced[recipes:recipes+10]), how_many


def main(recipes=RECIPES):
    ans1, ans2 = make_recipes(recipes)
    print("Part One:")
    print(f"The ten recipes after {recipes} others have scores {ans1}.")  # 3718110721

    print("\nPart Two:")
    print(f"The sequence first appears after {ans2} recipes.")  # 20298300
    src.copy(ans2)


if __name__ == '__main__':
    main()
