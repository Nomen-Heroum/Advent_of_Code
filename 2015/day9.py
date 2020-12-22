import src
import itertools
import re

STRINGS = src.read(9)


def distances_cities(strings=STRINGS):
    dd = {}
    cities = []
    for s in strings:
        city1, city2, distance = re.split(r' to | = ', s)
        cities += [city1, city2]
        dd[tuple(sorted((city1, city2)))] = int(distance)
    return dd, list(set(cities))


def trip_length(city_order: tuple, distances):
    length = 0
    for i, city in enumerate(city_order[:-1]):
        key = tuple(sorted((city_order[i], city_order[i + 1])))
        length += distances[key]
    return length


def main(strings=STRINGS):
    print("Part One:")
    dd, cities = distances_cities(strings)
    perms = list(itertools.permutations(cities))
    lengths = [trip_length(p, distances=dd) for p in perms]
    shortest = min(lengths)
    print(f"Shortest trip has length {shortest}.")

    print("\nPart Two:")
    longest = max(lengths)
    print(f"Longest trip has length {longest}.")
    src.copy(longest)


if __name__ == '__main__':
    main()
