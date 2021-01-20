import src
from copy import deepcopy

PLAYERS = src.read('\n\n')


def play_combat(players, recursive=False):
    win = 0
    if max(players[1]) > max(players[0]):  # Props to /u/curious_sapi3n for this optimisation
        cache = [deepcopy(players)]
        while all(players):
            cards = [p.pop(0) for p in players]
            if recursive and all(len(players[i]) >= cards[i] for i in range(2)):
                _, win = play_combat([players[i][:cards[i]] for i in range(2)], recursive=True)
            else:
                win = max(range(2), key=lambda x: cards[x])
            players[win] += [cards[win], cards[(win + 1) % 2]]
            if players in cache:
                win = 0
                break
            else:
                cache.append(deepcopy(players))

    return players, win


def calculate_score(players, win):
    winner = players[win]
    return sum(card * (i+1) for i, card in enumerate(winner[::-1]))


def main(players=PLAYERS):
    print("Part One:")
    players = [[int(s) for s in players[i].splitlines()[1:]] for i in range(2)]
    ans1 = calculate_score(*play_combat(deepcopy(players)))
    print(f"The final score is {ans1}.")

    print("\nPart Two:")
    ans2 = calculate_score(*play_combat(deepcopy(players), recursive=True))
    print(f"The winner of Recursive Combat had {ans2} points.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
