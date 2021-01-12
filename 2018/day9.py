import src
from collections import deque

PLAYERS = 426
LAST_MARBLE = 72058


def play_marbles(players: int, last_marble: int):
    circle = deque([0])
    scores = [0] * players
    current_player = 0
    for marble in range(1, last_marble + 1):
        if marble % 23 != 0:
            circle.rotate(2)
            circle.append(marble)
        else:
            circle.rotate(-7)
            scores[current_player] += marble + circle.pop()
        current_player += 1
        current_player %= players
    return max(scores)


def main(players=PLAYERS, last_marble=LAST_MARBLE):
    print("Part One:")
    ans1 = play_marbles(players, last_marble)  # 424112
    print(f"The winning elf has a score of {ans1}.")

    print("\nPart Two:")
    ans2 = play_marbles(players, last_marble * 100)  # 3487352628
    print(f"The new winning elf's score is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
