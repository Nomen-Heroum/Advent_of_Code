import src
import itertools
import re

STRINGS = src.read()


def parse(strings):
    people = []
    scores = {}
    for s in strings:
        p1, score, p2 = re.split(r' would | happiness units by sitting next to |\.', s)[:3]
        people += [p1, p2]
        sgn, amt = score.split()
        score = int(amt) if sgn == 'gain' else -int(amt)
        scores[(p1, p2)] = score
    return list(set(people)), scores


def total_score(permutation, scores, version=1):
    total = 0
    n = len(permutation)

    if version == 1:
        m = n
    else:
        m = n - 1

    for i, p in enumerate(permutation[:m]):
        nxt = permutation[(i+1) % n]
        total += scores[(p, nxt)] + scores[(nxt, p)]
    return total


def main(strings=STRINGS):
    print("Part One:")
    people, scores = parse(strings)
    perms = list(itertools.permutations(people))
    table = [total_score(p, scores) for p in perms]
    best = max(table)
    print(f"The best seating arrangement has a score of {best}.")

    print("\nPart Two:")
    table2 = [total_score(p, scores, version=2) for p in perms]
    best2 = max(table2)
    print(f"The best seating with me in it has a score of {best2}.")
    src.clip(best2)


if __name__ == '__main__':
    main()
