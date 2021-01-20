import src
from collections import defaultdict
from copy import deepcopy

COMPONENTS = [tuple(int(n) for n in s.split('/')) for s in src.read()]
PINS = {n for tup in COMPONENTS for n in tup}  # All different numbers of pins
FITS = {}  # Dictionary that keeps track of what fits to what
for n in PINS:
    FITS[n] = defaultdict(list)
    for c in COMPONENTS:
        if n in c:
            other = c[1] if c[0] == n else c[0]
            FITS[n][other].append([sum(c), 1])


def simplify_fits(fits=None):
    fits = fits or deepcopy(FITS)

    def add_end(k, h, ln, num):
        fits[k][-1].append([h, ln])
        # fits[k][-1] = [max(fits[k][-1])]
        del fits[k][num]

    while any(sum(len(v) for v in d.values()) < 3 for d in fits.values()):
        to_delete = []
        for n in fits:
            dct = fits[n]
            if n in dct and len(dct) < 4:  # If there is a component with n pins on either side:
                del dct[n]  # Remove that component
                for key in dct:
                    dct[key][0][0] += 2 * n  # Add its strength to one of the others
                    dct[key][0][1] += 1  # And its length, too
                    break
            option_count = sum(len(v) for v in dct.values())
            if option_count == 2:  # If precisely two connectors have n pins at one end:
                heft = sum(v[0][0] for v in dct.values())  # Calculate their combined strength
                length = sum(v[0][1] for v in dct.values())  # And combined length
                keys = list(dct.keys())
                if -1 in keys:
                    key = max(keys)
                    add_end(key, heft, length, n)
                else:
                    fits[keys[0]][keys[1]].append([heft, length])
                    del fits[keys[0]][n]
                    fits[keys[1]][keys[0]].append([heft, length])
                    del fits[keys[1]][n]
                to_delete.append(n)
            elif option_count == 1:  # If only one components has n pins, it's an endpiece
                key = next(iter(dct))
                heft = dct[key][0][0]
                length = dct[key][0][1]
                add_end(key, heft, length, n)
                to_delete.append(n)
        for n in to_delete:
            del fits[n]
    return fits


SIMPLE_FITS = simplify_fits()


def find_strongest(fits=None):
    fits = fits or SIMPLE_FITS

    remaining = frozenset({(frozenset((a, b)), w, ln)
                           for a, dct in fits.items()
                           for b, properties in dct.items()
                           for w, ln in properties})

    # We do a search using nodes of the form (total strength, total length, end-pins, set of remaining components)
    start = 0, 0, 0, remaining
    built = {start}
    to_expand = {start}
    while to_expand:
        new = set()
        for node in to_expand:
            strength, ttl_length, pins, remaining = node
            for new_pins, properties in fits[pins].items():
                for heft, length in properties:
                    piece = (frozenset({pins, new_pins}), heft, length)
                    if piece in remaining:
                        new_strength = strength + heft
                        new_length = ttl_length + length
                        new_bridge = (new_strength, new_length, new_pins, remaining - {piece})
                        if new_bridge not in built:
                            if new_pins >= 0:
                                new.add(new_bridge)
                            built.add(new_bridge)
        to_expand = deepcopy(new)
    return max(built)[0], max(built, key=lambda tup: (tup[1], tup[0]))[0]


def main():
    ans1, ans2 = find_strongest()
    print("Part One:")
    print(f"The strongest possible bridge has strength {ans1}.")  # 1940

    print("\nPart Two:")
    print(f"The strongest longest possible bridge has strength {ans2}.")  # 1928
    src.clip(ans2)


if __name__ == '__main__':
    main()
