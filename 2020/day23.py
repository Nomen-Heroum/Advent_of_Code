"""Algorithm used courtesy of /u/surplus-of-diggity"""
import src  # My utility functions

CUPS = [int(c) for c in '942387615']


def move(neighbours, current, n):
    pick = current
    pickup = []
    for _ in range(3):
        pick = neighbours[pick]
        pickup.append(pick)

    target_cup = current - 1 or n
    while target_cup in pickup:
        target_cup = (target_cup - 1) or n

    next_cup = neighbours[pick]
    neighbours[pick] = neighbours[target_cup]
    neighbours[target_cup] = neighbours[current]
    neighbours[current] = next_cup
    current = next_cup
    return neighbours, current


def play(neighbours, start, moves=100):
    print(f"The crab is working...\r", end='')
    current = start
    n = max(neighbours)
    for mov in range(moves):
        neighbours, current = move(neighbours, current, n)
    return neighbours


def main(cups=None):
    cups = cups or CUPS

    print("Part One:")
    neighbours1 = [0] + [cups[(cups.index(i+1) + 1) % len(cups)] for i in range(len(cups))]
    neighs1 = play(neighbours1, cups[0])
    ans1 = ''
    current = 1
    for _ in range(len(cups) - 1):
        current = neighs1[current]
        ans1 += str(current)
    print(f"The final configuration is {ans1}.")

    print("\nPart Two:")
    neighbours2 = ([0] + [(cups + [10])[cups.index(i+1) + 1] for i in range(len(cups))]
                   + list(range(11, 1_000_001)) + [cups[0]])
    neighs2 = play(neighbours2, cups[0], moves=10_000_000)
    star1 = neighs2[1]
    star2 = neighs2[star1]
    ans2 = star1 * star2
    print(f"My stars are hidden under two cups with product {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
