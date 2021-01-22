import src  # My utility functions
import parse
import re

ARMIES = src.read('\n\n')
PATTERN = parse.compile('{:d} units each with {:d} hit points{}'
                        'with an attack that does {:d} {} damage at initiative {:d}')


def parse_army(army_string, pattern=PATTERN, boost=0):
    army = {}
    for line in army_string.splitlines()[1:]:
        units, hit_points, specifics, damage, dmg_type, initiative = pattern.parse(line)
        army[initiative] = {
            'units': units,
            'hit_points': hit_points,
            'immune': set(),
            'weak': set(),
            'damage': damage + boost,
            'dmg_type': dmg_type
        }
        for spec in re.sub(r'[,()]', '', specifics).split('; '):
            if 'immune' in spec:
                army[initiative]['immune'] = set(spec.split()[2:])
            else:
                army[initiative]['weak'] = set(spec.split()[2:])
    return army


def battle(armies, boost=0):
    def power(key):
        return groups[key]['units'] * groups[key]['damage']

    immune_system = parse_army(armies[0], boost=boost)
    infection = parse_army(armies[1])
    groups = {**immune_system, **infection}  # Dictionary of all groups, regardless of army
    units_left = None
    while immune_system and infection:
        new_units_left = sum(g['units'] for g in groups.values())
        if new_units_left == units_left:  # No units killed in the last round
            return None, False
        units_left = new_units_left

        # Target selection phase
        selection_order = sorted(groups, key=lambda k: (power(k), k), reverse=True)
        unpicked_immune = set(immune_system.keys())
        unpicked_infection = set(infection.keys())
        targets = {}
        for group in selection_order:  # Build the dictionary of targets
            is_friendly = group in immune_system
            choices = unpicked_infection if is_friendly else unpicked_immune
            if not choices:  # Nothing left to pick
                continue
            dmg_type = groups[group]['dmg_type']
            can_damage = {c for c in choices if dmg_type not in groups[c]['immune']}
            if can_damage:
                target = max(can_damage, key=lambda c: (dmg_type in groups[c]['weak'], power(c), c))
                targets[group] = (target, dmg_type in groups[target]['weak'])
                choices.remove(target)

        # Attacking phase
        attack_order = sorted(targets, reverse=True)
        for group in attack_order:
            if group in groups:  # Hasn't been killed off yet
                target, is_weak = targets[group]
                damage = power(group) * (2 if is_weak else 1)
                units_killed = damage // groups[target]['hit_points']
                groups[target]['units'] -= units_killed
                if groups[target]['units'] <= 0:
                    del groups[target]
                    if target in infection:
                        del infection[target]
                    else:
                        del immune_system[target]

    return sum(g['units'] for g in groups.values()), bool(immune_system)


def main(armies=ARMIES):
    print("Part One:")
    ans1, _ = battle(armies)  # 14854
    print(f"There are {ans1} units left in the winning army.")

    print("\nPart Two:")
    boost = 0
    ans2 = 0
    immune_wins = False
    while not immune_wins:
        boost += 1
        ans2, immune_wins = battle(armies, boost=boost)  # 3467
    print(f"With just enough boost, {ans2} units are left in the immune system.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
