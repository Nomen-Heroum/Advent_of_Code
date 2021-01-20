import src
import math
import numpy as np

BOSS = [100, 8, 2]
SHOP = {'Weapons': np.array([[8, 4, 0],
                             [10, 5, 0],
                             [25, 6, 0],
                             [40, 7, 0],
                             [74, 8, 0]]),
        'Armor': np.array([[0, 0, 0],
                           [13, 0, 1],
                           [31, 0, 2],
                           [53, 0, 3],
                           [75, 0, 4],
                           [102, 0, 5]]),
        'Rings': np.array([[0, 0, 0],
                           [0, 0, 0],
                           [20, 0, 1],
                           [25, 1, 0],
                           [40, 0, 2],
                           [50, 2, 0],
                           [80, 0, 3],
                           [100, 3, 0]])}


def player_wins(player, boss=None):
    boss = boss or BOSS

    play_dph = max(1, player[1] - boss[2])
    boss_dph = max(1, boss[1] - player[2])

    play_hitsneeded = math.ceil(boss[0]/play_dph)
    boss_hitsneeded = math.ceil(player[0]/boss_dph)

    if play_hitsneeded <= boss_hitsneeded:
        return True
    return False


def minwin_maxloss(hp=100, boss=None, shop=None):
    shop = shop or SHOP
    boss = boss or BOSS

    price_of_success = []
    cost_of_failure = []
    for weapon in shop['Weapons']:
        for armor in shop['Armor']:
            for i, ring1 in enumerate(shop['Rings'][:-1]):
                for ring2 in shop['Rings'][i+1:]:
                    cost, damage, defence = weapon + armor + ring1 + ring2
                    if player_wins([hp, damage, defence], boss):
                        price_of_success.append(cost)
                    else:
                        cost_of_failure.append(cost)
    return min(price_of_success), max(cost_of_failure)


def main():
    cheapest, expensive = minwin_maxloss()

    print("Part One:")
    print(f"The least gold you can spend to win is {cheapest}.")
    print("\nPart Two:")
    print(f"The most gold you can spend on losing is {expensive}.")

    src.clip(expensive)


if __name__ == '__main__':
    main()
