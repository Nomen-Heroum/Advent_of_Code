import src  # My utility functions
from copy import deepcopy

BOSS = {'Hit Points': 71, 'Damage': 10}
PLAYER = {'Hit Points': 50, 'Mana': 500}


def fight(boss: dict, player: dict, version=1):
    boss_dmg = boss['Damage']
    states = {(boss['Hit Points'],  # initial state
               player['Hit Points'],
               player['Mana'],
               0, 0, 0, 0)}
    wins = set()
    losses = set()
    player_turn = True
    while states:
        new_states = set()
        for state in states:
            bh, ph, m, s, p, r, c = state

            if wins and c >= min(wins):  # You can win cheaper
                continue

            if ph <= 0:  # Player dies
                losses.add(c)
                continue

            s = max(0, s - 1)  # Shield cooldown
            if p:  # Poison effect
                p -= 1
                bh -= 3
            if r:  # Recharge effect
                r -= 1
                m += 101

            if bh <= 0:  # Boss dies
                wins.add(c)
                continue

            if player_turn:
                if version > 1:
                    ph -= 1
                if m < 53 or ph <= 0:  # Player runs out of mana
                    losses.add(c)
                    continue

                if m >= 53:  # Cast Magic Missile
                    new_states.add((bh - 4, ph, m - 53, s, p, r, c + 53))

                    if m >= 73:  # Cast Drain
                        new_states.add((bh - 2, ph + 2, m - 73, s, p, r, c + 73))

                        if not s and m >= 113:  # Cast Shield
                            new_states.add((bh, ph, m - 113, 6, p, r, c + 113))

                        if not p and m >= 173:  # Cast Poison
                            new_states.add((bh, ph, m - 173, s, 6, r, c + 173))

                        if not r and m >= 229:  # Cast Recharge
                            new_states.add((bh, ph, m - 229, s, p, 5, c + 229))

            else:  # The boss attacks
                new_states.add((bh, ph - boss_dmg + bool(s)*7, m, s, p, r, c))
        states = deepcopy(new_states)
        player_turn = not player_turn

    return min(wins)


def main(boss=None, player=None):
    boss = boss or BOSS
    player = player or PLAYER

    print("Part One:")
    ans1 = fight(boss, player)
    print(f"The least amount of mana you can spend and still win is {ans1}.")

    ans2 = fight(boss, player, version=2)
    print(f"On hard mode, you have to spend at least {ans2} mana.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
