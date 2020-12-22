import src

BOSS = {'Hit Points': 71, 'Damage': 10}
PLAYER = {'Hit Points': 50, 'Mana': 500}
SPELLS =


def fight(boss):
    pass


def main(boss=None):
    boss = boss or BOSS

    src.one()
    ans1 = fight(boss)
    print(f"The least amount of mana you can spend and still win is {ans1}.")
    
    src.copy(ans1)


if __name__ == '__main__':
    main()
