import src

STRINGS = src.read()


def intersect(strings):
    directions = {'L': -1, 'R': 1, 'U': 1j, 'D': -1j}
    wires = []
    for s in strings:
        wire = {}
        position = 0
        steps = 0
        for piece in s.split(','):
            direction = directions[piece[0]]
            for _ in range(int(piece[1:])):
                position += direction
                steps += 1
                if position not in wire:
                    wire[position] = steps
        wires.append(wire)
    intersections = wires[0].keys() & wires[1].keys()
    closest_intersection = int(min(abs(z.real) + abs(z.imag) for z in intersections))
    fastest_intersection = min(wires[0][z] + wires[1][z] for z in intersections)
    return closest_intersection, fastest_intersection


def main(strings=STRINGS):
    ans1, ans2 = intersect(strings)
    print("Part One:")
    print(f"The closest intersection is at distance {ans1} from the central port.")  # 1519

    print("\nPart Two:")
    print(f"The fewest combined steps taken to reach any intersection is {ans2}.")  # 14358
    src.clip(ans2)


if __name__ == '__main__':
    main()
