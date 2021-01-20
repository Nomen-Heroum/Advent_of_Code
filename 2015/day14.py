import src
import parse
import numpy as np

STRINGS = src.read()
END_TIME = 2503
PATTERN = parse.compile("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.")


def distance(string, end_time=END_TIME):
    _, speed, endurance, rest = PATTERN.parse(string)
    t = 0
    dist = 0
    rested = True
    while t < end_time:
        if rested:
            dist += min([endurance, end_time - t]) * speed
            t += endurance
        else:
            t += rest
        rested = not rested
    return dist


def main(strings=STRINGS, end_time=END_TIME):
    print("Part One:")
    furthest = max(distance(s, end_time) for s in strings)
    print(f"The winning reindeer got to {furthest} km.")

    print("\nPart Two:")
    scores = np.zeros(len(strings))
    for t in range(1, end_time + 1):
        distances = np.array([distance(s, t) for s in strings])
        most = np.max(distances)
        winners = np.array([int(d == most) for d in distances])
        scores += winners
    winning_score = int(np.max(scores))
    print(f"The highest score after {end_time}s is {winning_score}.")
    src.clip(winning_score)


if __name__ == '__main__':
    main()
